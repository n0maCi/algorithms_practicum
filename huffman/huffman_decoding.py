huffman_codes = {
    ' ': '1011',
    '.': '1110',
    'D': '1000',
    'c': '000',
    'd': '001',
    'e': '1001',
    'i': '010',
    'm': '1100',
    'n': '1010',
    'o': '1111',
    's': '011',
    'u': '1101'
}

encoded_string = "100011110001001101000111111011001010011000010110011010111110"

reverse_huffman_codes = {v: k for k, v in huffman_codes.items()}
def huffman_decode(encoded_string, reverse_huffman_codes):
    decoded_string = ""
    buffer = ""
    for bit in encoded_string:
        buffer += bit
        if buffer in reverse_huffman_codes:
            decoded_string += reverse_huffman_codes[buffer]
            buffer = ""
    return decoded_string
decoded_string = huffman_decode(encoded_string, reverse_huffman_codes)
print(decoded_string)
