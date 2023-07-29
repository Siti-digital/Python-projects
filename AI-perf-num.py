print("perfect number")
print("""
    Check if a number is perfect number or not
    A number which is the sum of all its divisors is a perfect number
    Eg:- 6=3+2+1
""")

x=int(input("Enter any number:-"))
a=1
b=0
while a<x:
    if x%a==0:
        b=b+a
    a=a+1

if b==x:
    print(" HURRAY!",x,"is a perfect number")
else:
    print(" ALAS!",x,"is not a perfect number")