print(""" 
    Prime number check """)
i=0

while i<1:
    x=int(input(" Enter a positive integer:- "))
    y,z,a=x,1,2
    print("""
        Processing......
        It might take few seconds to few minutes
         depending on the number 
        """)
    if x!=1:
        while a!=y:
            if y%a==0:
                z,a=0,y
                print(x,"is a composite number")
            else:
                a=a+1
        if z!=0:
            print(x,"is a prime number")
    elif x==1:
        print("1 is neither prime nor composite")
    
    t=str(input(" Do you again want to check another number (y/n) "))
    if t=='y':
        i=0
    elif t=='n':
        i=2

print(" Program ended ")

