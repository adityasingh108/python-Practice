
num1 = int(input("Enter the firist number:"))
num2 = int(input("enter the second number:"))
operator = input("Select the operator + - * / % :")


if num1 == 45 and num2 == 3 and operator == "*":
    print("555")
elif num1 == 56 and num2 == 9 and operator == "+":
    print("77")
elif num1 == 56 and num2 == 6 and operator == "/":
    print("4")

elif operator == "+":
    addition = num1+num2
    print(addition)
elif operator == "-":
    substraction = num1-num2
    print(substraction)
elif operator == "*":
    multiply = num1*num2
    print(multiply)

elif operator == "%":
    percent = num1 % num2
    print(percent)
else:
    print("plaese tyr again .^.")
