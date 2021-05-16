x = 60
def aadi():
    x= 80
    print(x)
    def mithu():
        global x
        # print(x)
        print("before aadi calling ",x)
    mithu()    
    
aadi()
