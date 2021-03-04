from typing import List, Callable, Sequence

def string_to_unicode(s: str) -> List[int]:
    return [ord(c) for c in s]

def unicode_list_to_string(lst: List[int]) -> str:
    return ''.join([chr(c) for c in lst])

def get_random_list_from_sequence(lenght: int, seq: Sequence) -> List:
     from random import choice
     return [ choice(seq) for i in range(lenght) ]

def random_string(lenght: int) -> str:
    from string import printable
    return ''.join(get_random_list_from_sequence(lenght, printable))

def get_file_contents(path: str) -> str:
    contents = None
    with open(path, 'r') as file:
        contents = file.read()
    return contents

def write_to_file(path: str, content: str) -> None:
    with open(path, 'w+') as file:
        file.write(content)

def combine_by(lst1: List, lst2: List, transform: Callable) -> List:
    lst_len = min(len(lst1), len(lst2))
    return [ transform(lst1[i], lst2[i]) for i in range(lst_len) ]

def get_random_int_list(lenght: int) -> List[int]:
    from random import shuffle
    list = [i for i in range(lenght)]
    shuffle(list)
    return list

def reorder_list(lst: List, order_list: List[int]) -> List:
    return [ lst[i] for i in order_list ]

def deorder_list(lst: List, order_list: List[int]) -> List:
    length = min(len(lst), len(order_list))
    tupled = [ (order_list[i], lst[i]) for i in range(length) ]
    tupled.sort(key=lambda x: x[0])
    return [ x[1] for x in tupled ]

def enc_dec_main(encrypt: Callable, decrypt: Callable):
    from sys import argv

    if len(argv) == 1:
        print("message to encrypt is required")
    
    if len(argv) == 2:
        msg = get_file_contents(argv[1])
        emsg, key = encrypt(msg)
        write_to_file('encrypted_msg.txt', emsg)
        write_to_file('key.txt', key)
    else:
        emsg = get_file_contents(argv[1])
        key = get_file_contents(argv[2])
        print(decrypt(emsg, key))