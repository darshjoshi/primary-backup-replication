# client.py

import socket
import sys
from common import send_message, recv_message
from config import PRIMARY_HOST, PRIMARY_PORT

def send_cmd(cmd, key, value=None):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((PRIMARY_HOST, PRIMARY_PORT))
    req = {'cmd': cmd, 'key': key}
    if value is not None:
        req['value'] = value
    send_message(sock, req)
    resp = recv_message(sock)
    sock.close()
    return resp

def repl():
    print(">> Commands: SET <key> <value>  |  GET <key>  |  EXIT")
    while True:
        line = input(">> ").strip()
        if not line:
            continue
        parts = line.split(maxsplit=2)
        cmd = parts[0].upper()
        if cmd == 'EXIT':
            break
        if cmd == 'SET' and len(parts) == 3:
            resp = send_cmd('SET', parts[1], parts[2])
        elif cmd == 'GET' and len(parts) == 2:
            resp = send_cmd('GET', parts[1])
        else:
            print("Invalid syntax")
            continue
        print("->", resp)

if __name__ == '__main__':
    try:
        repl()
    except KeyboardInterrupt:
        sys.exit(0)
