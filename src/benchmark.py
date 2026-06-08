from src.multicodec import MultiCodecCompressor


def benchmark(input_file):

    compressor = MultiCodecCompressor()

    codecs = [
        "gzip",
        "bz2",
        "lzma",
        "brotli",
        "zstd"
    ]

    results = []

    for codec in codecs:

        result = compressor.compress(
            input_file,
            codec
        )

        ratio = (
            result["compressed_size"]
            / result["original_size"]
        ) * 100

        result["ratio"] = ratio

        results.append(result)

    return results