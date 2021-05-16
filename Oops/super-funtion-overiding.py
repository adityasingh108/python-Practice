class A:
    class_var= "i am in the class variavle in A"
    def __init__(self):
        self.class_var3= "i'm iside the class variable "
        self.special_var = "i'm special variable "


class  B(A):
    class_var1= "i'm in the class variable in the class B"
    def __init__(self):
        super().__init__()
        self.class_var3= "i'm inside the class in B"        


a= A()
b = B()



print(b.special_var)