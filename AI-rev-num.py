print("""
 This program will reverse any given integer
 """)
x=int(input("Enter any integer:- "))
y=x
b=x
a=1
c=0

while b>=10:
    a=a+1 #tell the number of digits in the number
    b=b//10 #print the leftmost digit of number

while a>0:
    d=y%10 #extract rightmost digit
    c=c+(d*(10**a)) #sum the extracted diguits
    y=y//10
    a=a-1

print("Reverse of",x,"is",c//10)

 