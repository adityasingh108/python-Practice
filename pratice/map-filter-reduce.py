############### MAP FUNCTION###########
lst = [1, 2, 33, 4, 56, 7, 8, 9, 5]


def square(num):
    return num * num


def cube(num):
    return num * num * num


mathe = [square, cube]

for i in lst:
    print(list(map(lambda x: x(i), mathe)))

################   filter function ##############
#
# lst2 = [1, 2, 33, 4, 56, 7, 8, 9, 5]
#
# # def Return_grater_6(num):
# #     return num >6
#
# print(list(filter(lambda x: x > 5, lst)))

################# reduce function #######
# from functools import reduce

# lst3 = [1, 2, 3, 4, 6, 7, 9, ]

# print(reduce(lambda x,y:x+y,lst3))