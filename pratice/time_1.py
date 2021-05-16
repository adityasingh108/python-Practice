import time 
x= time.asctime(time.localtime(time.time()))
def get_time():
    print(time.time())
#    time.sleep()
    print(x)



def gate_time1():
    print(time.time())
    time.sleep(2)
    global x
    
    print(x)
    print(time.time())

get_time()    
gate_time1()