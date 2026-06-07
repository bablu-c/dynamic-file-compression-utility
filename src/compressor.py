import os
from src.huffman import HuffmanCoding


class FileCompressor:

    def __init__(self):
        self.huffman = HuffmanCoding()

    def compress_file(self, input_path, output_path):

        with open(input_path, "r", encoding="utf-8") as file:
            text = file.read()

        self.huffman.build(text)

        encoded_text = self.huffman.encode_text(text)

        with open(output_path, "w") as file:
            file.write(encoded_text)

        original_size = os.path.getsize(input_path)
        compressed_size = os.path.getsize(output_path)

        ratio = (compressed_size / original_size) * 100

        return {
            "original_size": original_size,
            "compressed_size": compressed_size,
            "compression_ratio": ratio
        }