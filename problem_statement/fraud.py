def rohan(num):
    if num == 6:
        import random
        rand_num = random.randint(20, 24)
        
        table=[]
        for i in range(1,10):
            
            a= num *i
            if i == 3:
                table.insert(3,rand_num)
            table.append(a)
            return table
    
    else :
        table1 = []
        for i in range(1, 11):
            table1.append(num*i)
        return table1
def is_correct(table , num):
    table2= []
    for i in range(1,11):
        a=num*i
        table2.append(a)
    if table == table2:
        return table
    else:
        return table2   
    
    

if __name__ == "__main__":
    try:
        num = int(input("Enter the number :"))
    except:
        print("Enter number only")
        exit()    
    print(rohan(num))
    # table = rohan(num)
    # print(is_correct(table,num))   