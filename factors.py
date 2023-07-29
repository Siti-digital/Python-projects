# factor so of number
x=int(input("Enter a number:- "))
a=x//2
print("Factors of",x,"are:-")
for i in range(1,a+1):
    b=x%i
    if b==0:
        print(i)
    else:
        "nothing"
    i=i+1
