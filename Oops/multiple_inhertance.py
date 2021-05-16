class Employee:
    def __init__(self, nickname, salary, hobby):
        self.nickname = nickname
        self.salary = salary
        self.hobby = hobby

    def print_details(self):
        return f"the nickname is {self.nickname}\nthe salary is {self.salary}\nthe hobby is {self.hobby}"

    @classmethod
    def from_dash(cls, dash):
        dash_store = dash.split("-")
        return cls(dash_store[0], dash_store[1], dash_store[2])


class programmer:
    def __init__(self, language, aim):
        self.language = language
        self.aim = aim

    def print_programer(self):
        return f"language is  {self.language}\nAim is {self.aim}"

    @classmethod
    def from_dash(cls, dash):
        dash_store = dash.split("-")
        return cls(dash_store[0], dash_store[1])


class cool_dude(Employee, programmer):
    pass
    # def __init__(self, work):
    #     self.work = work

    # def print_cool_dude(self):
    #     return f"the work is {self.work}"

    # @classmethod
    # def from_dash(cls, dash):
    #     dash_store = dash.split("-")
    #     return cls(dash_store[0], dash_store[1], dash_store[2], dash_store[3], dash_store[4])


aditya = Employee("aadi","28989","listingmusic")
manish = programmer("python","data_scientist")


alok =cool_dude("aluk","648756","gaar_marana")



# print(aditya.print_details())
# print(manish.print_programer())

print(alok.print_details())


