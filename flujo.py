def isPrimeFor(num):
	
	if num<2:
		flag=False
	elif num==2:
		flag=True
	else:	
		flag=True
		for i in range (2, num-1):
			if num%i==0:
				flag=False
				break
	return flag
p=input("dame un numero: ")

if isPrimeFor(p):
	print("es primo")
else:
	print("no es primo")


