from pwn import xor

KEY1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
KEY2_KEY3 = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
FLAG_KEY1_KEY2_KEY3 = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")

# KEY2 ^ KEY1 ^ KEY1 = KEY2 - Self Inverse Property KEY1 ^ KEY1 = 0 - Identity Property KEY2 ^ 0 = KEY2

KEY1_KEY2_KEY3 = xor(KEY1, KEY2_KEY3)

flag = xor(FLAG_KEY1_KEY2_KEY3, KEY1_KEY2_KEY3)

print(flag.decode('utf-8'))
