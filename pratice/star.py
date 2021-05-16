n = int(input("enter the number "))
print("if you enter 0  then program returns normal star \n if you enter 1 progrm returns reverce star")
number =bool(input("enter the number 0 and 1"))
# if number==0:
#     number=True
# else:
#     number=False

if number==True:
    for i in range(n):
        for j in range(i+1):
            print("*",end="")
        print() 

elif number==False:
    for i in range(n):
        for j in range(i,n):
            print("*",end="")
        print()
