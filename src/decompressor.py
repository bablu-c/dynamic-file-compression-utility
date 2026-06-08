import pickle
from src.bit_utils import remove_padding


class FileDecompressor:

    def decompress_file(self, input_path, output_path):

        with open(input_path + ".codes", "rb") as meta:
            codes = pickle.load(meta)

        reverse_codes = {v: k for k, v in codes.items()}

        bit_string = ""

        with open(input_path, "rb") as file:

            byte = file.read(1)

            while byte:
                bits = bin(byte[0])[2:].rjust(8, "0")
                bit_string += bits
                byte = file.read(1)

        encoded_text = remove_padding(bit_string)

        current_code = ""
        decoded_text = ""

        for bit in encoded_text:

            current_code += bit

            if current_code in reverse_codes:
                decoded_text += reverse_codes[current_code]
                current_code = ""

        with open(output_path, "w", encoding="utf-8") as file:
            file.write(decoded_text)

        return decoded_text