n =8
no_of_guess = 1
print("you have only 5 attempt to finsh he number ")
while no_of_guess <=5:
    guss_number = int(input("Enter the number"))
    if guss_number >8:
        print("try with smaller number:")
    elif guss_number<8:
        print("try with larger number:")
    else:
        print("you won")
        print("no of times to finish the game:",no_of_guess)
        break
    print("number of guess to finish this attempt ",5-no_of_guess)
    no_of_guess +=1

    if no_of_guess>5:
        print("game over")        