class math:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def addition(self):
        return f"the  firist number is  {self.x}  the second numbr is {self.y} the addition is {self.x+self.y} "


add = math("x", "y")

x= input("enter the firisyt number : ")
y= input("Enter the second number : ")

print(add.addition())