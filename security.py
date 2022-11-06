# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 16:30:11 2022

@author: Shree
"""

from Cryptodome.Cipher import AES
import uuid
textToNum = lambda x: int.from_bytes(bytes(x, 'utf-8'), 'big')

def mac_address():
    uu=str(uuid.getnode())
    return uu

def encrypt(text,directory):
    uuid=mac_address()
    key = textToNum(uuid)
    key = key.to_bytes(32, 'big')    
    data = bytes(text, 'utf-8')
    aes = AES.new(key, AES.MODE_EAX)
    encrypted, mac = aes.encrypt_and_digest(data)
    nonce = aes.nonce
    en=open(directory,"w")
    en.write(encrypted)

def decrypt(directory):
    uuid=mac_address()
    key = textToNum(uuid)
    key = key.to_bytes(32, 'big')
    
    aes = AES.new(key, AES.MODE_EAX, nonce)
    try:
        data = aes.decrypt_and_verify(encrypted, mac)
        return data.decode()
    except Exception:
        return 'Data was tampered!'