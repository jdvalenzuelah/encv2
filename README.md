## Usage

## Transposition

#### Encrypt a file
```shell
$ python transposition.py test.txt
```

Will generate 2 files `encrypted_msg.txt`, with the encrypted message, and `key.txt`, with the key to decrypt a message.

#### Decrypt a file

Pass path to encrypted file and path to key file

```shell
$ py transposition.py enc.txt key.txt
```

will print to stdout the decrypted content

## Sustitution

#### Encrypt a file
```shell
$ python sustitution.py test.txt
```

Will generate 2 files `encrypted_msg.txt`, with the encrypted message, and `key.txt`, with the key to decrypt a message.

#### Decrypt a file

Pass path to encrypted file and path to key file

```shell
$ py sustitution.py enc.txt key.txt
```

will print to stdout the decrypted content


## Combined

#### Encrypt a file
```shell
$ python combined.py test.txt
```

Will generate 2 files `encrypted_msg.txt`, with the encrypted message, and `key.txt`, with the key to decrypt a message.

#### Decrypt a file

Pass path to encrypted file and path to key file

```shell
$ py combined.py enc.txt key.txt
```

will print to stdout the decrypted content
