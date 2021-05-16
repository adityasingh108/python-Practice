 ##this is the list copprehension which isusing to extrct the  mtrix
matrix = [
     [1, 2, 3, 4],
    [5, 6, 7, 8],
   [9, 10, 11, 12],
 ]
#
# print(matrix)



# list1 =[[x[i] for x in matrix] for i in range(4)]
# print(list1)

list1 = list(zip(*matrix))
print(list1)