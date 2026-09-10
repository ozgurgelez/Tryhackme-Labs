import string
from pwn import *

charset= string.ascii_letters + string.digits
enc_flag = bytes.fromhex("00093d233765201c363311390419332075133324152f026b26380d093012263509683226393f2a3a(Your encoded flag hex string here)")
part_flag = b"THM{"

part_key = xor(enc_flag, part_flag)[:4]

for c in charset:
    key = part_key + c.encode()
    dec_flag = xor(enc_flag, key).decode()

    if dec_flag[-1] == '}':
        print(f"Found key: {key.decode()}")
        print(f"Decrypted flag: {dec_flag}")
