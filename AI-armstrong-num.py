print("""Check if a given number is ARMSTRONG NUMBER or not
	 """)
x=int(input(" Enter any number:- "))
b=x
c=0
while b>=10:
    d=b%10
    c=c+(d**3)
    b=b//10

if x==c+1:
    print(" HURRAY!",x,"is an Armstrong number")
else:
    print(" ALAS!",x,"""is not an Armstrong number
    BETTER LUCK NEXT TIME""")