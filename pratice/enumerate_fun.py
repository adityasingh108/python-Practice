def speciel_fun():
    print("this is special function")
    list = ["aadi","mith","manish"]

    for index,item in enumerate(list):
        if index%2 ==0:
            print(item)
       


def normalfun():
    print("this is normal function")
    list1 = ["aad","mit","man"]
    i = 1
    for item in  list1:
        if i%2 !=0:
            print(item)
        i +=1            
normalfun() 

speciel_fun()