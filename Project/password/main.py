import random
from datetime import datetime
name = input("what is your name ")
if name =="fuck":
    raise Exception("Enter the valid name")
if name.isnumeric():
    raise Exception("Enter the valid name")
lenght = int(input("enter the password Lengh"))
# name = input("what is your name ")
time = datetime.now()
lower = "abcdefghijklmnopqrstuvwxyz"
uper = lower.upper()
symbol ="~!@#$%^&*(~!@#$%^&*()"
number="`1234567890"
pass_manager = lower+uper+symbol+number
password =''.join(random.sample(pass_manager,lenght))
with open("password.txt",'a')as f:
    f.write(f"({name}) ({password}) ({time})\n")

print(password)