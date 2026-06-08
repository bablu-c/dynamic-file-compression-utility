import gzip
import bz2
import lzma
import brotli
import zstandard as zstd
import time
import os


class MultiCodecCompressor:

    def compress(self, input_file, codec):

        with open(input_file, "rb") as f:
            data = f.read()

        start = time.time()

        if codec == "gzip":
            compressed = gzip.compress(data)

        elif codec == "bz2":
            compressed = bz2.compress(data)

        elif codec == "lzma":
            compressed = lzma.compress(data)

        elif codec == "brotli":
            compressed = brotli.compress(data)

        elif codec == "zstd":
            compressed = zstd.ZstdCompressor().compress(data)

        else:
            raise ValueError("Unsupported codec")

        elapsed = time.time() - start

        output_file = input_file + "." + codec

        with open(output_file, "wb") as f:
            f.write(compressed)

        return {
            "codec": codec,
            "original_size": os.path.getsize(input_file),
            "compressed_size": os.path.getsize(output_file),
            "time": elapsed
        }