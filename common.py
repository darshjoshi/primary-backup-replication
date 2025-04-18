# common.py

import json
import struct

def send_message(sock, msg: dict):
    """
    Prefixes each message with a 4-byte length header, then sends JSON.
    """
    data = json.dumps(msg).encode('utf-8')
    header = struct.pack('>I', len(data))
    sock.sendall(header + data)

def recv_message(sock):
    """
    Reads the 4-byte length header, then the JSON payload.
    Returns dict or None on disconnect.
    """
    header = sock.recv(4)
    if not header:
        return None
    (length,) = struct.unpack('>I', header)
    data = sock.recv(length)
    return json.loads(data.decode('utf-8'))
