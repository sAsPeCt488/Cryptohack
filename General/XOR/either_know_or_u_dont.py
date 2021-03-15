from pwn import xor
from binascii import unhexlify
import time

def xor_byte(data, key):
    return xor(data, key)

data = '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'
flag_format = 'crypto{'
decoded = unhexlify(data)
print(f"H3x D3c0d3d: {decoded}")

partial_key = xor_byte(decoded[:7], flag_format)

key = partial_key.decode('utf-8') + 'y'

print(f"Partial Key: {key}")
time.sleep(2)

key = key * int(len (decoded)/len(key))
key += key[:((len(decoded) - len(key))%len(key))]

print(f"Full Key: {key}")
time.sleep(2)

flag = xor_byte(decoded, key)

print("Flag: ", flag.decode('utf-8'))
