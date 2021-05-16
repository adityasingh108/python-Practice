
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
    def change_number(cls, newnumber):
        cls.Number_of_Employee = newnumber

    @classmethod
    def from_str(cls, string):
        str_store = string.split("-")
        return cls(str_store[0], str_store[1], str_store[2])


class program(Employee):
    def __init__(self, nickadiname, salary, hobby, language):
        super().__init__(nickadiname, salary, hobby)
        self.nickname = nickadiname
        self.salary = salary
        self.hobby = hobby
        self.language = language

    def programer(self):
        return f"Nickname is: {self.nickname} \n Salary  is:{self.salary}\n hobby is:{self.hobby} \n  the language is {self.language}"

    @classmethod
    def from_str(cls, string):
        str_store = string.split("-")
        return cls(str_store[0], str_store[1], str_store[2], str_store[3])


Rohan = Employee("Rondhu", " 2000", "To paly cricket ")
Rahul = Employee("Lauru", "35000", "To paly Football ")
Ravi = program("lands", "40000", " to play bollyboll", "python")

alok = program.from_str("laura-100000-gaming-java")

print(Ravi.programer())
