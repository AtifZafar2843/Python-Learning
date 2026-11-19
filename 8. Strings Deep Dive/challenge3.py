# Challenge:


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
