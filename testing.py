# Testing with userinput (password)

import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

password = input("password ").encode()
if password == b'password_inp':
    inp = input("encrypt your message: ").encode()
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    f = Fernet(key)

    token = f.encrypt(inp)
    saved_msg = open("saving.msg","wb")
    saved_msg.write(token)
    saved_msg.close()
    print(token)

    de = f.decrypt(token)
    print(de)

else:
    print("GTFO!!! you fool hackeer.......")