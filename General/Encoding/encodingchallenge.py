from pwn import * # pip install pwntools
import json
import base64, binascii, codecs, time
from Crypto.Util.number import long_to_bytes

r = remote('socket.cryptohack.org', 13377)

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

def base64_decode(data):
    decoded = base64.b64decode(data).decode('utf-8').replace("'", '"')
    return decoded

def hex_decode(data):
    decoded  = bytes.fromhex(data).decode('utf-8').replace("'", '"')
    return decoded

def rot13_decode(data):
    decoded  = codecs.decode(data, 'rot_13')
    return decoded

def bigint_decode(data):
    data =  data.replace("0x", "")
    longint  = bytes.fromhex(data)
    decoded  = longint.decode('utf-8').replace("'", '"')
    return decoded

def utf_8_decode(data):
    decoded  = ""
    for num in data:
        char = chr(num)
        decoded = decoded + char
    return decoded

funcs = {
        'base64':base64_decode,
        'hex': hex_decode,
        'rot13': rot13_decode,
        'bigint':bigint_decode,
        'utf-8':utf_8_decode
}


def decode(data):
    return funcs[data['type']](data['encoded'])


for stage in range(100):
    received = json_recv()
    data = received["encoded"]
    encoding = received["type"]
    print(f"[Stage {str(stage)}] Received - {received['encoded']}")
    solution = decode(received)
    print(f'[Stage {str(stage)}] - Sending {solution}')

    to_send = {
        "decoded": solution
        }
    json_send(to_send)


received = json_recv()
print("========== Finished ==========")
print(f"\nFlag: {received['flag']}")
