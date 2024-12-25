class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

def build_frequency_dict(text):
    frequency = {}
    for char in text:
        if char not in frequency:
            frequency[char] = 0
        frequency[char] += 1
    return frequency

def build_priority_queue(frequency):
    nodes = []
    for char, freq in frequency.items():
        nodes.append(Node(char, freq))
    return nodes

def build_huffman_tree(nodes):
    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.freq)

        left = nodes.pop(0)
        right = nodes.pop(0)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        nodes.append(merged)

    return nodes[0]

def build_codes_helper(root, current_code, codes):
    if root is None:
        return

    if root.char is not None:
        codes[root.char] = current_code
        return

    build_codes_helper(root.left, current_code + "0", codes)
    build_codes_helper(root.right, current_code + "1", codes)

def build_codes(root):
    codes = {}
    build_codes_helper(root, "", codes)
    return codes

def encode(text, codes):
    encoded_text = ""
    for char in text:
        encoded_text += codes[char]
    return encoded_text

def huffman_encoding(text):
    frequency = build_frequency_dict(text)
    nodes = build_priority_queue(frequency)
    root = build_huffman_tree(nodes)
    codes = build_codes(root)
    encoded_text = encode(text, codes)
    return encoded_text, root, codes

def print_huffman_results(text):
    encoded_text, root, codes = huffman_encoding(text)
    print(len(codes), len(encoded_text))
    for char, code in sorted(codes.items()):
        print(f"'{char}': {code}")
    print(encoded_text)

text = "Errare humanum est."
print_huffman_results(text)
