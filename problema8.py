divisor=1
n = int(input("ingrese el numero : ")) 
while divisor <= n:
    res=n % divisor
    if res == 0 :
        print(divisor)
    divisor +=1