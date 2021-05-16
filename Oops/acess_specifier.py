# public = it start with single underscore in python  as for example _public in python
# protected = it srtart with the  _ underscore in the python  as
# private = this acessifire in python  it start with the doble underscore in the python
#          as for example  __private in python 
#                and it call with the help of class  class-name__private varibale-name 

class Employee:
    Number_of_Employee = 52     # this is the public varible  or it can be access by the all the instance and all thec class
    _name_ofcompany = "tata"    #this is protected variable 
    __passwoird_of_company = "aadi@qwe"

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

print(Rohan._name_ofcompany)
print(Rohan._Employee__passwoird_of_company)   #this is the name angelin in the python 



