def recursion(n):
    if n ==0:
        print("hello")
    else:
        print(n  ,end="  ") 
        recursion(n-1) 

n = int(input(""))    

print(recursion(n))