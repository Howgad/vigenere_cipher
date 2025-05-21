def vigenere_cipher(text: str, key: str, mode: str = 'encrypt') -> str:
    if not key.isalpha():
        raise ValueError("Key must consist of letters only")

    result = []
    key = key.upper()
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            base = ord('A') if char.isupper() else ord('a')

            if mode == 'encrypt':
                shifted = (ord(char) - base + shift) % 26 + base
            elif mode == 'decrypt':
                shifted = (ord(char) - base - shift) % 26 + base
            else:
                raise ValueError("Mode must be 'encrypt' or 'decrypt'")

            result.append(chr(shifted))
            key_index += 1
        else:
            result.append(char)

    return ''.join(result)


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 4:
        print("Usage: python -m vigenere_cipher.vigenere <encrypt|decrypt> <key> <text>")
        sys.exit(1)

    mode, key, text = sys.argv[1], sys.argv[2], ' '.join(sys.argv[3:])
    print(vigenere_cipher(text, key, mode))