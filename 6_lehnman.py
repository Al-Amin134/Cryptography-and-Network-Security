import random

'''
Task number 6
Prime Number check by Lehnmann algorithm
'''
def isprime(p,k=5):
# p is the number and k is the iteration number
	if p<=1 :
		return False
	elif p<=3 :
		return True
	elif p%2==0:
		return False
	else :
		for _ in range(k):
			a = random.randint(2,p-2)
			z = pow(a,(p-1)//2, p)
			if z!=1 and z!=p-1:
				return False
		return True
p = int(input("Enter number p: "))
if isprime(p):
	print("Probably Prime")
else:
	print("Not prime")

