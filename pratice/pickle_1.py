# import pickle
# car ={car:f"car{car}" for car in range(5)}
# file_obj = open("imahe.png",'wb')
# pickle_dump = pickle.dump(car,file_obj)

import pickle
file = 'imahe.png'
file_obj = open(file,'rb')
car = pickle.load(file_obj)
print(car)