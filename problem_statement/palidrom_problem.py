"""
Author :Aditya
Date :16-05-2021
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
    return str(n) == str(n)[::-1]  ## simply reverse the number or string 


if __name__ == "__main__":

    try:
        # takes the  number of input  from the user
        number_input = int(input("Enter the number of text cases"))
    except:
        print("Enter number only")
        exit()
    list_of_number = []  # Blank list in which we store the number enter by the user
    for i in range(number_input):
        try:
            user = int(input("Number should be greater than 0:"))
        except:
            print("Enter Number only")
            exit()
        if user != 0:
            list_of_number.append(user)
        else:
            print("Warning !! number should be grater than 0")
            exit()

    for i in range(number_input):  # in this listed the palandromic number
        print(
            f"{list_of_number[i]} next palindrom is {next_palindrome(list_of_number[i])}")

    # print(is_palindrome.__doc__)                 ### doc string retrev
