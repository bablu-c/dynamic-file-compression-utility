import argparse

from src.compressor import FileCompressor
from src.decompressor import FileDecompressor
from src.verify import verify_files
from src.benchmark import benchmark


def compress_command(input_file):

    compressor = FileCompressor()

    output_file = input_file.split("/")[-1]
    output_file = output_file.replace(".txt", ".huff")
    output_file = "compressed_files/" + output_file

    result = compressor.compress_file(
        input_file,
        output_file
    )

    print("\nCompression Report\n")

    print("Original Size :", result["original_size"], "bytes")
    print("Compressed Size :", result["compressed_size"], "bytes")
    print(
        "Compression Ratio :",
        round(result["compression_ratio"], 2),
        "%"
    )


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


def benchmark_command(input_file):

    results = benchmark(input_file)

    print("\nBenchmark Results\n")

    print("-" * 60)

    for r in results:

        print(
            f"{r['codec']:10} | "
            f"{r['compressed_size']:8} bytes | "
            f"{r['ratio']:.2f}% | "
            f"{r['time']:.4f}s"
        )

    print("-" * 60)


parser = argparse.ArgumentParser(
    description="Dynamic File Compression Utility"
)

parser.add_argument(
    "action",
    choices=[
        "compress",
        "decompress",
        "verify",
        "benchmark"
    ]
)

parser.add_argument(
    "file",
    nargs="?",
    default=None
)

args = parser.parse_args()

if args.action == "compress":

    if not args.file:
        print("Please provide input file")
    else:
        compress_command(args.file)

elif args.action == "decompress":

    if not args.file:
        print("Please provide compressed file")
    else:
        decompress_command(args.file)

elif args.action == "verify":

    verify_command()

elif args.action == "benchmark":

    if not args.file:
        print("Please provide input file")
    else:
        benchmark_command(args.file)