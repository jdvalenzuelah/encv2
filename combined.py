from typing import Tuple
from common import enc_dec_main
from transposition import encrypt as enc_trans
from transposition import decrypt as dec_trans
from sustitution import encrypt as enc_sus
from sustitution import decrypt as dec_sus
import json

def encrypt(msg: str) -> Tuple[str]:
    msg1, key1 = enc_trans(msg)
    msg2, key2 = enc_sus(msg1)
    keys = { '1': key1, '2':key2 }
    return msg2, json.dumps(keys)

def decrypt(msg: str, key: str) -> str:
    keys = json.loads(key)
    msg1 = dec_sus(msg, keys['2'])
    return dec_trans(msg1, keys['1'])

if __name__ == '__main__':
    enc_dec_main(encrypt, decrypt)