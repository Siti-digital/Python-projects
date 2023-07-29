# program contain some extra things wasn't known to me at the time of creation
# program code is copied from different source

print(" Print 3 different patterns upto a given number of rows")
x=int(input("Input the number of rows:- "))

print(""" PATTERN 1 
""")
for a in range(1,x+1):
    y='* '                 
    print(a*y)

print(""" PATTERN 2
 """)
for b in range(0,x+1):
    for j in range(1,5-b+1):
        print(j,end="")
    print("")

print(" PATTERN 3 ")
if x<=26:
    for i in range(0,x+1,1):
        for j in range(65,65+i):
            print(chr(j),end=' ')
        print("")
else:
    print("Pattern 3 is only printed when no. of rows is <= 26")