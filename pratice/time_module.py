import time
 
# initial= time.asctime(time.localtime(time.time()))
# print(initial)
# print(time.localtime(time.time()))


initial= time.time()


a=0
while(a<100):
    print("this is time ")
    a = a+1                                                               
print("while loop run in ",time.time()-initial)    

initial2= time.time()

for i in range(1000):
    print("this is Time")
print("for loop takes time ",time.time()-initial2)    



