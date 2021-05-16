import pickle
import requests

url ="https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
get_data = requests.get(url).text
# print(get_data)
list1= list(get_data.split("\n"))
main_data = [item.split(",") for item in list1 if len(item) !=0]
with open("pickle.img","wb") as file:
    pickle.dump(main_data,file)


files = 'pickle.img'
with open(files,"rb") as f:
    pickle.load(f,files)   