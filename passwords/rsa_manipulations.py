from passwords.config import *
import rsa


def create_keys(key_size: int = Constants.KEY_SIZE) -> tuple[bytes, bytes]:
    """
        Generate keys, pub and priv for user
    :param key_size:
    :return:
    """
    public_key, private_key = rsa.newkeys(key_size)
    return public_key.save_pkcs1(), private_key.save_pkcs1()


def crypt_password(pub_key: bytes, password: str) -> bytes:
    """
        Encrypt password , return encrypt password in bytes
    :param pub_key:
    :param password:
    :return:
    """
    pub_key = rsa.PublicKey.load_pkcs1(pub_key)
    encrypted_pass = rsa.encrypt(password.encode(), pub_key)
    return encrypted_pass


def decrypt_password(private_key: bytes, password: bytes) -> str:
    """
        Decrypt password, return password in str
    :param private_key:
    :param password:
    :return:
    """
    private_key = rsa.PrivateKey.load_pkcs1(private_key)
    password = rsa.decrypt(password, private_key)
    return password.decode('utf-8')
