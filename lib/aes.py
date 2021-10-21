import secrets
import base64, hashlib
from Crypto import Random
from Crypto.Cipher import AES

def random_str_gen(n=32):
    '''
    Return a n-bit or n/8-byte key for AES encryption.
    '''
    return secrets.token_urlsafe(n)

class AESCipher(object):

    def __init__(self, key): 
        self.bs = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw.encode()))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]

if __name__ == '__main__':
    key = random_str_gen(32)
    print(key)
    password = 'Csc346Z@'
    new_key = key[0:-len(password)] + password
    print(new_key)

    clear = 'HelloAggie'
    print('Before encryption:', clear)
    aes = AESCipher(new_key)
    cipher = aes.encrypt(clear)
    aes2 = AESCipher(new_key)
    clear = aes2.decrypt(cipher)
    print('Encryption:', cipher)
    print('After decryption:', clear)

