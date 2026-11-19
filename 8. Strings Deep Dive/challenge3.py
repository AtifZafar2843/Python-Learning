# Challenge:
# Build an encoder and a decoder for a Caesar cipher with a given shift.

# Rules:
# • Shift letters by the given amount, wrapping around (z + 1 -> a)
# • Preserve case (uppercase stays uppercase, lowercase stays lowercase)
# • Leave non-letters (spaces, digits, punctuation) unchanged

# Demonstrate a round-trip: encode a message, then decode it back to the original to prove it matches.

# Example (shift = 3):

# Original: Hello, Tab47!
# Encoded:  Khoor, Wde47!
# Decoded:  Hello, Tab47!

# Hint: ord() and chr() convert between characters and their number codes.

# Solution:
def encode(text, shift):
    encoded_text = ""

    for char in text:
        if char.isupper():
            code = ord(char) + shift
            if code > ord('Z'):
                code -= 26
            encoded_text += chr(code)

        elif char.islower():
            code = ord(char) + shift
            if code > ord('z'):
                code -= 26
            encoded_text += chr(code)

        else:
            encoded_text += char

    return encoded_text

def decode(text, shift):
    decoded_text = ""

    for char in text:
        if char.isupper():
            code = ord(char) - shift
            if code < ord('A'):
                code += 26
            decoded_text += chr(code)

        elif char.islower():
            code = ord(char) - shift
            if code < ord('a'):
                code += 26
            decoded_text += chr(code)

        else:
            decoded_text += char

    return decoded_text

text = "Hello this is Atif Zafar, this message is very secret!"
shift = 3

encoded_text = encode(text, shift)
decoded_text = decode(encoded_text, shift)

print(f"Original: {text}")
print(f"Encoded: {encoded_text}")
print(f"Decoded: {decoded_text}")
