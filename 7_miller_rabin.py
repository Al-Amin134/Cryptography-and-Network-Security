import random

'''
Task number 7
Prime Number check by Miller Rabin algorithm
'''
def isprime(p,k=5):
# p is the number and k is the iteration number
	if p<=1 :
		return False
	if p<=3 :
		return True
	if p%2==0:
		return False
	
		
	 # (p-1) = 2^b*m
	 # 2<a<p-2
	 # z = a^m mod p
	 # if z = 1 or z = p-1 continue
	 # z = z^2 (until b times)
	 # if z = p-1 break
	 #return false
	m = p-1
	b = 0
	while(m%2==0):
	 	m//=2
	 	b+=1
	for _ in range(k):
	 	a = random.randint(2,p-2)
	 	z = pow(a,m,p)
	 	if z ==1 or z ==p-1:
	 		continue
	 	for _ in range(b-1):
	 		z = pow(z,2,p)
	 		if z==p-1:
	 			break
	 	else:
	 		return False# ey else er mane hlo puro inner loop a z = p-1 payni tai return false kreche
	return True
	 
	 
		
	
p = int(input("Enter number p: "))
if isprime(p):
	print("Probably Prime")
else:
	print("Not prime")


