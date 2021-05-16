import math 



def distance(x1,y1,x2,y2):
    ds = x2-x1
    dy = y2-y1
    dsquare = ds**2 + dy**2
    result = math.sqrt(dsquare)
    return result


x1= int(input("eter the value of x1:"))    
x2= int(input("eter the value of x2:"))
y1= int(input("eter the value of y1:"))
y2= int(input("eter the value of y2:"))


print(distance(x1,x2,y1,y2))