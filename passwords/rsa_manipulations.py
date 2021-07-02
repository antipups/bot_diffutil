from passwords.config import *
import rsa


def create_keys(key_size: int = Constants.KEY_SIZE) -> tuple[bytes, bytes]:
    public_key, private_key = rsa.newkeys(key_size)
    return public_key.save_pkcs1(), private_key.save_pkcs1()


