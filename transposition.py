from typing import Tuple
from common import *

def encrypt(msg: str) -> Tuple[str]:
    key = get_random_int_list(len(msg))
    encrypted = reorder_list(list(msg), key)
    return ''.join(encrypted), '-'.join([str(c) for c in key])

def decrypt(msg: str, key: str) -> str:
    key_ints = [ int(c) for c in key.split('-') ]
    return ''.join(deorder_list(list(msg), key_ints))

if __name__ == '__main__':
    enc_dec_main(encrypt, decrypt)