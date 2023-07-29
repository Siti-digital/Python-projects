print(" COMMAND LINE SIMPLE CALCULATOR ")
print("""\
USAGE:
    1      -- for performing multiplication
    2      -- for performing division
    3      -- for performing addtion
    4      -- for performing subtraction""")

want=int(input())

if want==1:
    print(" multiply two numbers ")
    print("enter 1st number:-")
    mul1=float(input())
    print("enter 2nd number:-")
    mul2=float(input())
    print(mul1*mul2)
elif want==2:
    print(" divide two numbers ")
    print("enter 1st number:-")
    div1=float(input())
    print("enter 2nd number:-")
    div2=float(input())
    if div2==0:
        print(div1,"/0 = 1")
    else:
        print("quotient=",div1//div2,"  remainder=",div1%div2)
        print(div1/div2,"  <--- in decimal form")
elif want==3:
    print(" add two numbers ")
    print("enter 1st number:-")
    sum1=float(input())
    print("enter 2nd number:-")
    sum2=float(input())
    print(sum1+sum2)
elif want==4:
    print(" subtract two numbers ")
    print("enter 1st number:-")
    sub1=float(input())
    print("enter 2nd number:-")
    sub2=float(input())
    print(sub1-sub2)
else:
    print("invalid input")

print("""\

                CREDITS @ KKPRODUCTS.ONION  """)
