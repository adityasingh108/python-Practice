def search_name():
    word = []
    Employee_number = int(input("How many Employee you want to add this company"))
    for i in range(Employee_number):
        user_inp = input("enter the Company member ")
        word.append(user_inp)
    print("Your comapny member list is ",word)    
    # Book = ["aditya","singh"]

    while True:
        user_sercher = (yield)
        if user_sercher in list(word):
            print("Your Member in the comany")
        else:
            print("Another one is tring to enter the company")


if __name__ =="__main__":
    no_of_time = 1
    while no_of_time:
        user= input("enter Start to start the program\nAnd enter s to stop the program ")
        if user =="start":
            comany_employee =search_name()
            next(comany_employee)
            user_seching = input("Enter the Member name to clearify the status")
            comany_employee.send(user_seching)
        elif user=="s":
            print("You have sucessfully mange your companty name ")    

        break         