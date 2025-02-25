from transformations import block_encryption, deploying_keys, block_decryption
from errors import KeyLengthError
import base64


def encryption(path_to_file: str, key: str, path_to_output_file: str):
    with open(path_to_file, "rb") as read_file:
        read_file.seek(0, 2)
        last_pos = read_file.tell()
        read_file.seek(0)
        key_binary = bytearray(base64.b64decode(key))
        if len(key) != 32:
            raise KeyLengthError
        keys = deploying_keys(key_binary)
        with open(path_to_output_file, "wb") as output_file:
            len_of_last_block = int()
            while read_file.tell() != last_pos:
                current_block = bytearray(read_file.read(16))
                len_of_last_block = len(current_block)
                if len(current_block) != 16:
                    current_block.extend((16-len(current_block))*(bytearray([0x00])))
                output_file.write(block_encryption(current_block, keys))
            output_file.write((16 - len_of_last_block).to_bytes(1, byteorder="big"))


def decryption(path_to_file: str, key: str, path_to_output_file: str):
    with open(path_to_file, "rb") as read_file:
        read_file.seek(0, 2)
        last_pos = read_file.tell()
        read_file.seek(0)
        key_binary = bytearray(base64.b64decode(key))
        if len(key) != 32:
            raise KeyLengthError
        keys = deploying_keys(key_binary)
        if len(keys) != 32:
            raise KeyLengthError
        with open(path_to_output_file, "wb") as output_file:
            while read_file.tell() != last_pos:
                current_block = bytearray(read_file.read(16))
                if len(current_block) == 16:
                    output_file.write(block_decryption(current_block, keys))
                else:
                    output_file.seek(-current_block[0], 2)
                    output_file.truncate()
