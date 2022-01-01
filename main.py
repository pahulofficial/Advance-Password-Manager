# Just playing with library and trying different things 

from cryptography.fernet import Fernet

message = input("Enter password ")

seceret_key = Fernet.generate_key()

# saving the value of seceret-key 
 
saved_key = Fernet(seceret_key)
print(saved_key)
token = saved_key.encrypt(message.encode())

var = open("save.txt","w")
var.write(str(saved_key))
var.close()
print(token)

dec_token  = saved_key.decrypt(token).decode()

print(dec_token)