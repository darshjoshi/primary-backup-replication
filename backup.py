# backup.py

import socket
import threading
import time

from config import BACKUP_HOST, BACKUP_PORT, HEARTBEAT_TIMEOUT
from common import send_message, recv_message

store = {}
last_heartbeat = time.time()
promoted = threading.Event()

def monitor_heartbeat():
    global last_heartbeat
    while not promoted.is_set():
        time.sleep(1)
        if time.time() - last_heartbeat > HEARTBEAT_TIMEOUT:
            print("[BACKUP] Missed heartbeat → promoting to primary!")
            promoted.set()
            break

def handle_primary(conn):
    global last_heartbeat
    with conn:
        while True:
            msg = recv_message(conn)
            if msg is None:
                break
            if msg.get('cmd') == 'HEARTBEAT':
                last_heartbeat = time.time()
            elif msg.get('cmd') == 'SET':
                store[msg['key']] = msg['value']

def serve_clients():
    # once promoted, start serving GET requests on PRIMARY port
    import socket
    from config import PRIMARY_HOST, PRIMARY_PORT

    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.bind((PRIMARY_HOST, PRIMARY_PORT))
    srv.listen()
    print(f"[NEW PRIMARY] Listening for clients on {PRIMARY_HOST}:{PRIMARY_PORT}")
    while True:
        conn, addr = srv.accept()
        threading.Thread(target=handle_client, args=(conn,), daemon=True).start()

def handle_client(conn):
    from common import send_message, recv_message
    with conn:
        while True:
            req = recv_message(conn)
            if req is None:
                break
            if req.get('cmd') == 'GET':
                key = req['key']
                send_message(conn, {'status':'OK','value':store.get(key)})
            else:
                send_message(conn, {'status':'ERROR','error':'Not primary'})

def main():
    # listen for primary on BACKUP port
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.bind((BACKUP_HOST, BACKUP_PORT))
    srv.listen()
    print(f"[BACKUP] Listening for primary on {BACKUP_HOST}:{BACKUP_PORT}")

    # start heartbeat watcher
    threading.Thread(target=monitor_heartbeat, daemon=True).start()

    # accept primary connection
    conn, _ = srv.accept()
    print("[BACKUP] Connected to primary")
    handle_primary(conn)

    # if promoted, close old socket and serve clients
    if promoted.is_set():
        srv.close()
        serve_clients()

if __name__ == '__main__':
    main()
