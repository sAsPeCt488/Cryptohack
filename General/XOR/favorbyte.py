from binascii import unhexlify
import time
from pwn import *

def xor_byte(data, key):
    return xor(data, key)

decoded  = unhexlify("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

print('H3x D3c0d3d: ', decoded)
time.sleep(1)

for byte in range(256):
    result = xor_byte(decoded, byte)
    try:
        output = result.decode('utf-8')
        if 'crypto' in output:
            break
    except:
        pass
print(f'Flag: {output}')
