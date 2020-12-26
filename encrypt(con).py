import crypting

print("Encrypt:1 Decrypt:2")
enorde = int(input(":"))
print("Password")
password = input(":")
print("File or Directory name")
filename = input(":")

if enorde == 1:
    crypting.encrypt_auto(filename, password, 'saltysalt')
if enorde == 2:
    crypting.decrypt_auto(filename, password, 'saltysalt')
else:
    print("Invalid input")
input("Done")
