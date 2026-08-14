import random

def diffie_hellman():
	p = 23
	a = 5
	print(f"The prime random prime number is: {p}")
	print(f"The primitive root is {a}")
	
	#publicly shared_key
	xa , xb = random.randint(2,p-2), random.randint(2,p-2)
	print(f"publicly shared key : xa = {xa}, xb = {xb}")
	
	#private key
	ya = pow(a,xa,p)
	yb = pow(a,xb,p)
	print(f"private key for Alice is: {ya}")
	print(f"private key for Bob is : {yb}")
	
	#exchange the key
	sa = pow(yb,xa,p)
	sb = pow(ya,xb,p)
	print(f"Secret key for Alice is: {sa}")
	print(f"Secret key for Bob is : {sb}")
	
	if sa==sb:
		print("Key Exchance is Succeed")
	else:
		print("Failed")
		
if __name__=="__main__":
	diffie_hellman()
