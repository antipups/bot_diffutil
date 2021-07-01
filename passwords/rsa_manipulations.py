from passwords.config import *
import rsa


def create_key(key_size: int = Constants.KEY_SIZE):
    public_key, private_key = rsa.newkeys(key_size)


