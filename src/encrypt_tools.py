import secrets
import base64
import hashlib
import bcrypt
from Crypto import Random
from Crypto.Cipher import AES


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
        return self._unpad(
            cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]


def random_str_gen(n=32):
    '''
    Return a n-bit or n/8-byte key for AES encryption.
    '''
    return secrets.token_urlsafe(n)


def forge_secret_key(tag_random_str: str, pin: str) -> str:
    """
    This function merges the tag random string with the 
    pin, then hash them using SHA3-512 to create the final 
    secret key for unlock a user's password vault.
    """
    merged_key = tag_random_str[0:-len(pin)] + pin
    m = hashlib.sha3_256(merged_key.encode('utf-8'))
    return m.hexdigest()


def encrypt_data(secret_key: str, data: str):
    aes = AESCipher(secret_key)
    return aes.encrypt(data).decode('utf-8')


def decrypt_data(secret_key: str, data: str):
    aes = AESCipher(secret_key)
    return aes.decrypt(data)


def generate_pin_salt():
    return bcrypt.gensalt()


if __name__ == '__main__':
    print(generate_pin_salt())
