def print_message(*numbers):
    for item in numbers:
        print(item)
        


list = []
# list_len = len(list)
a= int(input("How many Books you want to add "))
for item in range(a):
    usr_input= input("Enter Book name\n:")
    list.append(usr_input)
print_message(*list)
print(print_message(*list))

