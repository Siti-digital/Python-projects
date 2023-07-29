print(""" 
    Print a list of prime numbers upto a certain number
     """)
x=int(input("Upto which number? "))
y=x
z=y
a=2
b=a

if x==1:
    print(" ERROR! 1 is neither prime nor composite ")
elif x!=1:
    while z!=1:
        while b!=z:
            if z%b==0:
                b=z
               # print(z,"is composite")
            elif z%b!=0:
                b=b+1
                if b==z-1:
                    print(z,"is prime")
        b=a   
        z=z-1
print("3 is prime")   
print("2 is prime")