import heapq
from collections import Counter


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


class HuffmanCoding:

    def __init__(self):
        self.heap = []
        self.codes = {}
        self.reverse_codes = {}

    def build_frequency_table(self, text):
        return Counter(text)

    def build_heap(self, frequency):
        for char, freq in frequency.items():
            heapq.heappush(self.heap, Node(char, freq))

    def build_huffman_tree(self):
        while len(self.heap) > 1:
            left = heapq.heappop(self.heap)
            right = heapq.heappop(self.heap)

            merged = Node(None, left.freq + right.freq)
            merged.left = left
            merged.right = right

            heapq.heappush(self.heap, merged)

        return heapq.heappop(self.heap)

    def generate_codes(self, node, current_code=""):

        if node is None:
            return

        if node.char is not None:
            self.codes[node.char] = current_code
            self.reverse_codes[current_code] = node.char
            return

        self.generate_codes(node.left, current_code + "0")
        self.generate_codes(node.right, current_code + "1")

    def build(self, text):
        freq = self.build_frequency_table(text)
        self.build_heap(freq)
        root = self.build_huffman_tree()
        self.generate_codes(root)

    def encode_text(self, text):
        return "".join(self.codes[ch] for ch in text)

    def decode_text(self, encoded_text):

        current = ""
        decoded = ""

        for bit in encoded_text:

            current += bit

            if current in self.reverse_codes:
                decoded += self.reverse_codes[current]
                current = ""

        return decoded

    def print_frequency_table(self, text):

        freq = self.build_frequency_table(text)

        print("\nFrequency Table\n")

        for char, count in freq.items():
            print(f"{repr(char)} : {count}")

    def print_codes(self):

        print("\nHuffman Codes\n")

        for char, code in self.codes.items():
            print(f"{repr(char)} -> {code}")