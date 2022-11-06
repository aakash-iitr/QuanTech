#from Cryptodome.Cipher import AES
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
    encrypted = aes.encrypt_and_digest(data)
    en=open(directory,"w")
    en.write(encrypted)
    return directory



def decrypt(directory):
    
    uuid=mac_address()
    key = textToNum(uuid)
    key = key.to_bytes(32, 'big')
    en=open(directory,"r")
    encrypted=en.read()
    aes = AES.new(key, AES.MODE_EAX)
    try:
        data = aes.decrypt_and_verify(encrypted)
        return data.decode()
    except Exception:
        return 'Data was tampered!'
