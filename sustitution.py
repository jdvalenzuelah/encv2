from typing import Tuple, List
from common import *

def encrypt(msg: str) -> Tuple[str]:
    key = random_string(len(msg))
    encrypt_fun = lambda x, y: x+y
    encrypted = unicode_list_to_string(combine_by(string_to_unicode(msg), string_to_unicode(key), encrypt_fun))
    return encrypted, key

def decrypt(msg: str, key: str) -> str:
    decrypt_fun = lambda x, y: x-y
    return unicode_list_to_string(combine_by(string_to_unicode(msg), string_to_unicode(key), decrypt_fun))

if __name__ == '__main__':
    enc_dec_main(encrypt, decrypt)