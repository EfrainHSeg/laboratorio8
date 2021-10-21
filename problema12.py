valor= 0
divisor=0
n =int(input("ingrese numero "))
while divisor <=n:
    divisor+=1
    if n % divisor == 0:
        valor +=1
if valor ==2:
    print("primo")
else:
    print("no primo")       
    
    
    
