def main():##acreate a main function which takes nothing 
    try:
        user = int(input("Enter your Age or Birth year"))#store the age or year in the user variable 

    except:
        print("\nplease Enter number only") # if user enter other than intingr the the program exit with the error
        exit()    

    if len(str(user)) > 3:# if user lenhth is more the 3 this means year of birth
        if user <=2021 and user > 1900:#if birth year more the 1900 and leesser than 2021
            print(f"You are turn 100 at {100-(2021-user)} Years later")#print this statemenet
        elif user > 2021:#or year of birth more than 2021 
            print(f"you are not Yet to born Lol!")#print thiis statement
        elif user<1900:##if birth year less thn 1900 
            print("You seem to the oldest peron alive")#print this statement



    if len(str(user)) <= 3:#if lenth of the user 3 and less than 3 means this is age
        if user == 100:# if age is is eqal to 100  
            print("You are at the age of 100")
        elif user > 100:# or age is more than 100
            print("You seem to the oldest peron alive")
        else:#
            print(f"You are getting 100 at {100 - user} years later")


if __name__ == '__main__':# this is the main function of python 
    while(True): # infinite lopp 
        main()