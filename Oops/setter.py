class  Employee:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname= lname
        

    def print(self):
        return f"the Employee is {self.fname}{self.lname}"


    @property
    def email(self):
        return f"{self.fname}.{self.lname}@gmail.com"


    @email.setter
    def email(self,String):
        Str_store = String.split("@")[0]
        self.fname =Str_store.split(".")[0]
        self.lname = Str_store.split(".")[1]


    
        






hindustani_supporter= Employee("hINDUSTANI","supporter")




print(hindustani_supporter.email)

hindustani_supporter.email = "this.that@gmail.com"


print(hindustani_supporter.email)




