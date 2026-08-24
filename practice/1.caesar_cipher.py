def caesar_cipher(text, shift):
    result = ""
    for c in text:
        if c==' ':
            result+=c
        else:
            if c.isupper():
                base = ord('A')
            else:
                base = ord('a')
            cipher = ord(c)-base
            cipher = (cipher+shift)%26
            result+=chr(cipher+base)
    return result


text = "The name of my country is Bangladesh"
cipher = caesar_cipher(text, 3)
plain_text = caesar_cipher(cipher, -3)

print(f"Ciphertext: {cipher}")
print(f"Decrypted text: {plain_text}")

