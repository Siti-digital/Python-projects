print("""
 This will print the sum of digits of a given integer
  """)

x=int(input("Enter any integer:- "))
y,a,b=x,x,0
while a!=0:
    y=a%10
    a=a//10
    b=b+y

print("Sum of the digits of",x,"is",b)
  
    
