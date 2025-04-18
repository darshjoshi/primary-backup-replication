# primary.py

import socket
import threading
import time

from config import PRIMARY_HOST, PRIMARY_PORT, BACKUP_HOST, BACKUP_PORT, HEARTBEAT_INTERVAL
from common import send_message, recv_message

store = {}  # in‑memory key→value

def handle_client(conn, addr, backup_sock):
    with conn:
        while True:
            req = recv_message(conn)
            if req is None:
                break
            cmd = req.get('cmd')
            if cmd == 'SET':
                key, val = req['key'], req['value']
                # 1) apply locally
                store[key] = val
                # 2) replicate to backup
                send_message(backup_sock, {'cmd':'SET','key':key,'value':val})
                # 3) ack to client
                send_message(conn, {'status':'OK'})
            elif cmd == 'GET':
                key = req['key']
                val = store.get(key)
                send_message(conn, {'status':'OK', 'value': val})
            else:
                send_message(conn, {'status':'ERROR','error':'Unknown cmd'})

def heartbeat_loop(backup_sock):
    while True:
        time.sleep(HEARTBEAT_INTERVAL)
        send_message(backup_sock, {'cmd':'HEARTBEAT'})

def main():
    # connect to backup
    backup_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    backup_sock.connect((BACKUP_HOST, BACKUP_PORT))

    # start heartbeat thread
    threading.Thread(target=heartbeat_loop, args=(backup_sock,), daemon=True).start()

    # start listening for clients
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.bind((PRIMARY_HOST, PRIMARY_PORT))
    srv.listen()
    print(f"[PRIMARY] Listening on {PRIMARY_HOST}:{PRIMARY_PORT}")

    try:
        while True:
            conn, addr = srv.accept()
            print(f"[PRIMARY] Client connected: {addr}")
            threading.Thread(target=handle_client, args=(conn, addr, backup_sock), daemon=True).start()
    except KeyboardInterrupt:
        print("Shutting down primary.")
    finally:
        srv.close()
        backup_sock.close()

if __name__ == '__main__':
    main()
