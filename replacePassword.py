import hashlib
import binascii

newPass = input("What would you like to replace as the new password?\n")

print("Opening exe file for read write permissions")
f = open("33056145.program2.exe", "rb+")

# f.read(16*7743)
# f.seek(4321766)
f.seek(16*7742 + 6)
# print(f.read(20))

hashVal = hashlib.sha1(newPass.encode()).hexdigest().upper()

print("New SHA1 hashed value %s" %(hashVal))

print("Overwriting address 0x0041F1E6 with new hased value ")
f.write(binascii.unhexlify(hashVal))
f.close()