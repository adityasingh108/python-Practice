import re
file_name = input("Enter the file name :")
Email_string = open(file_name, "r")
Email_read = Email_string.read()
email = re.findall(r"\w+@\S+\w", Email_read)
list1 = list(email)
i = 1
with open("Email.txt", "w") as file:
    for item in list1:
        file.write(f"{i} {item}\n")
        i = i+1

