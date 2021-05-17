##This is the problem statement 
"""
Author :Aditya
Date :15-05-2021
prrpose :problem solving
"""

if __name__ == "__main__":  # main function
    # input the size of the list
    try:
        lenth = int(input("how many item you want to store in the List:"))
    except:
        print("Please Enter number only:") 
        exit()   

    list1 = []  # Create blank list
    for i in range(lenth):  # looping the to create the list
        try:
            # ask user to enter the element in the list
            user = int(input("Enter the Calory:"))
            list1.append(user)  # put the element in the list
        except:
            print("Please Enter intinger only")  # error handing
            exit()    # if error occur program exit

    try:
        
        main_list = sorted(list1)  # sort the list using sort function

        firist_list = main_list#initialize the sorted list into firist list 
        firist_list.reverse()# reverse the list using reverse function
        print(f"The firist method is {firist_list}")

        second_list = main_list#initialize the secod list
        second_list[::-1]#reverse the ist using siling
        print(f"The second  method is {second_list}")


        third_list = main_list[::]#initialize the third list
        for i in range(len(third_list)):#looping in range of number of elements in the list divide by the half time 
            third_list[i],third_list[len(third_list)-i -1]=third_list[len(third_list)-i -1],third_list[i]   ##wap the last element into the firist element
        print(f"The third method {third_list}")
        

        if firist_list==second_list and second_list==third_list:#compare the all list 
            print("all list are same")
        else:
            print("List are not same ")    

    except:
        print("Error!")
