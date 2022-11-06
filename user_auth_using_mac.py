# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 21:31:36 2022

@author: DELL
"""

from cryptography.fernet import Fernet
import uuid, base64

def mac_address():
    
    uu=str(uuid.getnode())
    """s=""
    for i in uu :
        s=s+chr(i)"""
    uu_bytes = uu.encode("ascii")

    base64_bytes = base64.urlsafe_b64encode(uu_bytes)
    base64_string = base64_bytes.decode("ascii")
    return base64_bytes

def encryption(msg):
    
    key=mac_address()
    message=msg.encode()
    f=Fernet.generate_key()
    encrypted_message=f.encrypt(message)
    return encrypted_message

def decryption(msg):
    key=mac_address()
    f=Fernet(key)
    decrypted_message=f.decrypt(msg)
    return decrypted_message

a=input("message")
d=encryption(a)
print(d)
e=decryption(d)
print(e)
