data = 'label'
integer = 13
flag = ''
for char in data:
    flag += chr(ord(char) ^ integer)

print('Flag: crypto{', flag, '}')
