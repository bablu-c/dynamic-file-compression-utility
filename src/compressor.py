import os
import pickle

from src.huffman import HuffmanCoding
from src.bit_utils import pad_encoded_text, get_byte_array


class FileCompressor:

    def __init__(self):
        self.huffman = HuffmanCoding()

    def compress_file(self, input_path, output_path):

        with open(input_path, "r", encoding="utf-8") as file:
            text = file.read()

        self.huffman.build(text)

        encoded_text = self.huffman.encode_text(text)

        padded_encoded_text = pad_encoded_text(encoded_text)

        byte_array = get_byte_array(padded_encoded_text)

        with open(output_path, "wb") as output:
            output.write(bytes(byte_array))

        with open(output_path + ".codes", "wb") as meta:
            pickle.dump(self.huffman.codes, meta)

        original_size = os.path.getsize(input_path)
        compressed_size = os.path.getsize(output_path)

        ratio = (compressed_size / original_size) * 100

        return {
            "original_size": original_size,
            "compressed_size": compressed_size,
            "compression_ratio": ratio
        }