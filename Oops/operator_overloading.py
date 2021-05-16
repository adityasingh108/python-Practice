class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary


    def print_details(self):
       return f"the bname is {self.name} the salary is {self.salary}"    


    def __add__ (self,other):
        return self.salary+ other.salary        



    def __mull__(self,other):
        return self.salary * other.salary   


    def __truediv__(self,other):
        return self.salary / other.salary
      


emp = Employee("aditya",2333)
emp1= Employee("moni",244)   


print(emp+emp1)
print(emp/emp1)