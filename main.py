import argparse

from src.compressor import FileCompressor
from src.decompressor import FileDecompressor
from src.verify import verify_files


def compress_command(input_file):

    compressor = FileCompressor()

    output_file = input_file.replace(".txt", ".huff")

    output_file = "compressed_files/" + output_file.split("/")[-1]

    result = compressor.compress_file(
        input_file,
        output_file
    )

    print("\nCompression Report\n")

    print("Original Size :", result["original_size"], "bytes")
    print("Compressed Size :", result["compressed_size"], "bytes")
    print("Compression Ratio :", round(result["compression_ratio"], 2), "%")


def decompress_command(input_file):

    decompressor = FileDecompressor()

    output_file = input_file.split("/")[-1]

    output_file = output_file.replace(".huff", ".txt")

    output_file = "decompressed_files/" + output_file

    decompressor.decompress_file(
        input_file,
        output_file
    )

    print("\nDecompression Successful")
    print("Output:", output_file)


def verify_command():

    status = verify_files(
        "input_files/sample.txt",
        "decompressed_files/sample.txt"
    )

    print("\nVerification:", status)


parser = argparse.ArgumentParser(
    description="Dynamic File Compression Utility"
)

parser.add_argument(
    "action",
    choices=["compress", "decompress", "verify"]
)

parser.add_argument(
    "file",
    nargs="?",
    default=None
)

args = parser.parse_args()

if args.action == "compress":

    compress_command(args.file)

elif args.action == "decompress":

    decompress_command(args.file)

elif args.action == "verify":

    verify_command()