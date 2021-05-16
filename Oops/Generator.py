
def fact(n):
    facte = 1
    for i in range (n):
        facte = facte * (i+1)
    yield facte

def fibbonaci(n):
    if n ==1:
        yield n
    elif n ==2:
        yield n 
    else:
        yield (n-1) +(n-2)               

if __name__=="__main__":
    n = int(input("Enter the number "))
    fact(n)
    fibbonaci(n)
    for item in fact(n):
        print(item)

    for item in fibbonaci(n):
        print(item)    
