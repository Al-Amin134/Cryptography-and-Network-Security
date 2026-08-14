import hashlib

def sha1(text):
	encoded_text = text.encode()
	hash_value = hashlib.sha256(encoded_text)
	return hash_value.hexdigest()
if __name__== '__main__' :
	text = input("Enter the text: ")
	hash_value = sha1(text)
	print(f"The original value is : {text}")
	print(f"The hash value is : {hash_value}")
