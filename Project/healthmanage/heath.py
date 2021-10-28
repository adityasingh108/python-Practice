
from datetime import datetime
def log(s):
    if s == 1:
        aadi_input = int(input("1 for food\n2 for exercise\n:>"))
        if aadi_input == 1:
            with open("aadi_food.txt", "a") as file_object:
                content = input("")
                file_object.write(f"{content} time{datetime.now()}\n")
                file_object.close()
        elif aadi_input == 2:
            with open("aadi_exercise.txt", "a") as file_object:
                content = input("")
                file_object.write(f"{content} time{datetime.now()}\n")
                file_object.close()
    elif s == 2:
        mithu_input = int(input("1 for food\n2 for exercise\n:>"))
        if mithu_input == 1:
            with open("mithu_food.txt", "a") as file_object:
                content = input()
                file_object.write(f"{content} time{datetime.now()}\n")
                file_object.close()
        elif mithu_input == 2:
            with open("mithu_exercise.txt", "a") as file_object:
                content = input("")
                file_object.write(f"{content} time{datetime.now()}\n")
                file_object.close()
    elif s == 3:
        subendu_input = int(input("1 for food\n2 for exercise\n:>"))
        if subendu_input == 1:
            with open("subendu_food.txt", "a") as file_object:
                content = input()
                file_object.write(f"{content} time{datetime.now()}\n")
                file_object.close()
        elif subendu_input == 2:
            with open("subendu_exercise.txt", "a") as file_object:
                content = input("")
                file_object.write(f"{content} time{datetime.now()}\n")
                file_object.close()


def retrive(r):
    if r == 1:
        aadi_input = int(input("1 for food\n2 for exercise\n:>"))
        if aadi_input == 1:
            with open("aadi_food.txt", 'r') as file_object:
                for line in file_object:
                    print(line, end="")
        elif aadi_input == 2:
            with open("aadi_exercise.txt", "r") as file_object:
                for line in file_object:
                    print(line, end="")
    if r == 2:
        mithu_input = int(input("1 for food\n2 for exercise\n:>"))
        if mithu_input == 1:
            with open("mithu_food.txt", 'r') as file_object:
                for line in file_object:
                    print(line, end="")
        elif mithu_input == 2:
            with open("mithu_exercise.txt", "r") as file_object:
                for line in file_object:
                    print(line, end="")
    if r == 3:
        subendu_input = int(input("1 for food\n2 for exercise\n:>"))
        if subendu_input == 1:
            with open("subendu_food.txt", 'r') as file_object:
                for line in file_object:
                    print(line, end="")
        elif subendu_input == 2:
            with open("subendu_exercise.txt", "r") as file_object:
                for line in file_object:
                    print(line, end="")


if __name__ == "__main__":
    while True:
        # a= input("Enter stop to Quit program")

        a = int(input("1 for Log the data \n0 for retrive the Data\n:>"))
        if a == 1:
            b = int(input("1 for Aadi\n2 for Mithu\n3 for Subendu\n:>"))
            log(b)
        elif a == 0:
            b = int(input("1 for Aadi\n2 for Mithu\n3 for Subendu\n:>"))
            retrive(b)
        break    

