# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# # Design a calculator which will correctly solve all the problems except
# # the following ones:
# # 45 * 3 = 555, 56+9 = 77, 56/6 = 4




def claculator(num1,num2,num3):
    if num1 == 45 and num2 == 3 and num3 == "*":
        print("555")
    elif num1 == 56 and num2 == 9 and num3 == "+":
        print("77")
    elif num1 == 56 and num2 == 6 and num3 == "/":
        print("4")
    elif num3 == "+":
        add = num1 + num2
        print(add)
    elif num3 == "-":
        subs = num1 - num2
        print(subs)
    elif num3 == "*":
        multiply = num1 * num2
        print(multiply)

    elif num3 == "/":
        divide = num1 / num2
        print(divide)
    elif num3 == "%":
        percent = num1 % num2
        print(percent)

    else:
        print("plaese try again ")



if __name__ =="__main__":
    while True:
        num1 =int(input("Enter the firist number :"))
        num2 =int(input("Enter the second number:"))
        num3 =input("what do u want + ,-,*,/,%:")
        claculator(num1, num2 , num3)
        user_input = str(input("Enter q to stop the program\nTo countinue the program Press any key\n"))
        if user_input == 'q':
            break
        if user_input == 'Q':
            break