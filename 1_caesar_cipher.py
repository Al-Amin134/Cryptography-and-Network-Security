def caesar_cipher(text, shift):
	result = ""
	for c in text:
		base = ord('A') if c.isupper() else ord('a')
		result+=chr((ord(c)-base+shift)%26+base)
	return result


plaintext = "UNIVERSITY OF RAJSHAHI"
print(f"Original:  {plaintext}")

encrypted = caesar_cipher(plaintext, 3)
print(f"Encrypted: {encrypted}")

decrypted = caesar_cipher(encrypted, -3)
print(f"Decrypted: {decrypted}")
