class number:
    def __init__(self,x ):
         self.x=x
    # def print_number(x):
    #     if x%2==0:
    #         print("number is Even")
    #     else:
    #         print("number is Odd ")  

    def recursion(x):
        if x ==0:
            print("hellow")
        else:
            print(x)
            x -=1              
    

odd_even = number("x")
x = int(input("enter a number"))

#print(number.print_number(a))
print(number.recursion(x))

