
def fact(n):
    facte = 1
    for i in range (n):
        facte = facte * (i+1)
    return facte

def fibbonaci(n):
    if n ==1:
        return n
    elif n ==2:
        return n 
    else:
        return (n-1) +(n-2)               

n = int(input("Enter the number "))
print(fact(n))
print(fibbonaci(n))
