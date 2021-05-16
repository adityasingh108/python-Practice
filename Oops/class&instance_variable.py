# now we create the instance variable and class variable
# we can't mutate the class variable with the help of instance
# but class variable mutate can manipulate its variable and the instance variable also manipulates


class Employee:
    amount_of_salery = int(20000)
    pass


Heigh_Level_Worker = Employee()
Low_Level_Worker = Employee()


Heigh_Level_Worker.name = "rahul"
Heigh_Level_Worker.work = "Coding"
Heigh_Level_Worker.hobby = "sutte"


Low_Level_Worker.name = "rohan"
Low_Level_Worker.work = "safai"
Low_Level_Worker.hobby = "to Singging"

# we also see that  where is varible defined or not defined with he help of
# __dict attributes

print("low level worker salary before the instace varible:",
      Low_Level_Worker.amount_of_salery)
print(Low_Level_Worker.__dict__)
# Here create the instance varible and assign to the object
Low_Level_Worker.amount_of_salery = int(10000)
print(" When Instace varible create the alary is :",
      Low_Level_Worker.amount_of_salery)
print(Low_Level_Worker.__dict__)


print(Employee.__dict__)
print("Before the class varible :", Employee.amount_of_salery)
# Now we create the class variable
Employee.amount_of_salery = int(400000)

print("after the class varible", Employee.amount_of_salery)
print(Employee.__dict__)
