
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
    def change_number(cls, Newnumber):
        cls.Number_of_Employee = Newnumber

    @classmethod
    def from_str(cls, string):
        str_store = string.split("-")
        return cls(str_store[0], str_store[1], str_store[2])


Rohan = Employee("Rondhu", " 2000", "To paly cricket ")
Rahul = Employee("Lauru", "35000", "To paly Football ")
Ravi = Employee.from_str("Gola-3400- to play football")


# Rohan.nickname ="Rondhu"
# Rohan.salary = 2000
# Rohan.hobby = "To paly cricket "


# Rahul.nickname ="Lauru"
# Rahul.salary = 35000
# Rahul.hobby = "To paly Football "
print(Ravi.details())
