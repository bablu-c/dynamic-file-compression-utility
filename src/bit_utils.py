def pad_encoded_text(encoded_text):

    extra_padding = 8 - len(encoded_text) % 8

    for _ in range(extra_padding):
        encoded_text += "0"

    padded_info = "{0:08b}".format(extra_padding)

    encoded_text = padded_info + encoded_text

    return encoded_text


def get_byte_array(padded_encoded_text):

    if len(padded_encoded_text) % 8 != 0:
        raise ValueError("Encoded text not padded correctly")

    byte_array = bytearray()

    for i in range(0, len(padded_encoded_text), 8):

        byte = padded_encoded_text[i:i+8]

        byte_array.append(int(byte, 2))

    return byte_array


def remove_padding(padded_encoded_text):

    padded_info = padded_encoded_text[:8]

    extra_padding = int(padded_info, 2)

    padded_encoded_text = padded_encoded_text[8:]

    encoded_text = padded_encoded_text[:-extra_padding]

    return encoded_text