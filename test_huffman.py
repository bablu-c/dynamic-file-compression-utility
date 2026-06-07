from src.huffman import HuffmanCoding

text = "dynamic file compression utility"

huffman = HuffmanCoding()

huffman.build(text)

huffman.print_frequency_table(text)

huffman.print_codes()

encoded = huffman.encode_text(text)

print("\nEncoded Text:\n")
print(encoded)

decoded = huffman.decode_text(encoded)

print("\nDecoded Text:\n")
print(decoded)

print("\nMatch:", text == decoded)