from src.compressor import FileCompressor

compressor = FileCompressor()

result = compressor.compress_file(
    "input_files/sample.txt",
    "compressed_files/sample.huff"
)

print("\nCompression Report\n")

print("Original Size :", result["original_size"], "bytes")
print("Compressed Size :", result["compressed_size"], "bytes")
print("Compression Ratio :", round(result["compression_ratio"], 2), "%")