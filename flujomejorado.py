def isprime(num):
   
    if num < 2:
        flag=False
       
    elif num==2:
        flag=True
       
    else:
        flag=True
        for i in range(2,num - 1):
            if num % i==0:
                flag=False
               
                break
    return flag
p=input("Dame un numero, ")
s=12

while s!=0:
    if p%2==0:
        p = p + 1
    while not isprime(p):
        p = p + 2
        if p%2==0:
            p=p+1
    while p<s:
            s = s - p
            p = p + 2
            if p%2==0:
                p = p + 1
            while not isprime(p):
                p=p+2
                if p%2==0:
                    p = p + 1
    s = s - 1
    if s!=0:
        p=p+2
             
print(p)   


