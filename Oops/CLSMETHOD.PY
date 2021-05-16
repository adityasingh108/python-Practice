# In this Lession we create the constructor


class Employee:
    Number_of_Employee = 52
    def __init__(self, nickadiname, salary, hobby):  # THIS IS CONSTRUCTOR
        self.nickname = nickadiname
        self.salary = salary
        self.hobby = hobby

    def details(self):
        # CREATE A FUNCTION THAT
        return f"Nickname is: {self.nickname} \n Salary  is:{self.salary}\n hobby is:{self.hobby}"
        # SHOW THE ALL PROPERTIES OF THE SELF
    @classmethod
    def  change_number(cls,Newnumber):
        cls.Number_of_Employee =Newnumber



Rohan = Employee("Rondhu", " 2000", "To paly cricket ")
Rahul = Employee("Lauru", "35000", "To paly Football ")


# Rohan.nickname ="Rondhu"
# Rohan.salary = 2000
# Rohan.hobby = "To paly cricket "


# Rahul.nickname ="Lauru"
# Rahul.salary = 35000
# Rahul.hobby = "To paly Football "

Employee.change_number(0)
print(Employee.Number_of_Employee)
# print(Rahul.details(