from cryptography.fernet import Fernet
key = Fernet.generate_key()
encryptor = Fernet(key)

file2 = 'mainfile.txt'
print(file2)

with open(file2,'rb')as x:
    x_file = x.read()

file3 = encryptor.encrypt(x_file)

with open(file2,'wb')as y:
    y.write(file3)

print(f'this is the key to decrypt:',str(key,'utf8')
