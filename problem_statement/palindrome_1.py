"""
Author :Aditya
Date :17-05-2021
prrpose :problem solving
"""


def next_palindrome(n):
    """ This Function if the number 
    is not palandromic, the whole function should be 
    return True"""
    n = n+1
    while not is_palindrome(n):
        n += 1
    return n


def is_palindrome(n):
    """This function return the number which is 
    palindromic number """
    return str(n) == str(n)[::-1]  # simply reverse the number or string


if __name__ == "__main__":
    list1 = []  ###blank list
    for i in range(5): # iterate the loop 5 times to ask  to user to  input the number  in the  List 

        try:
            user = int(input("Enter the number "))
        except:
            print("Enter number only")
        list1.append(user)  ## append the  numer in the list 
    print("Input List's number :", list1) # show the list

    palindrom_list = [] #Blank list of palindromic number 
    for item in list1: #jitna item list mai hai utna baar loop chalega 
        if item > 10: # if the item is more  than the 10
            n = next_palindrome(item) # to run function to the item  
            palindrom_list.append(n) # add the item in the palindromic _list
        else: #othervise
            palindrom_list.append(item) # number added to palandromic_list
    print("Output list's number:", palindrom_list) # show the palandromi list
