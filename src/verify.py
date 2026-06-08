def verify_files(original_path, decompressed_path):

    with open(original_path, "r", encoding="utf-8") as f1:
        original = f1.read()

    with open(decompressed_path, "r", encoding="utf-8") as f2:
        decompressed = f2.read()

    return original == decompressed