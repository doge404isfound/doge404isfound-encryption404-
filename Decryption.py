from cryptography.fernet import Fernet

file4 = input('enter key:')
key = file4
decryptor = Fernet(key)
with open('mainfile.txt','rb')as z:
    z_data = z.read()
Decrypted_data = decryptor.decrypt(z_data)

with open('mainfile.txt','wb') as z:
    z.write(Decrypted_data)
print('file is Decrypted')
