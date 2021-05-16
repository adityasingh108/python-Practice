import os
# from posix import listdir
def pretify_folder(path,file,format):
    os.chdir(path)
    i = 1
    files =os.listdir(path)
    with open(file) as f:
        file_list = f.read().split("\n")

    for file in files:
        if file != file_list:
            os.rename(file ,file.capitalize())
        if  os.path.splitext(file)[1] == format:
            os.rename(file ,f"{i}{format}")
            i +=1

pretify_folder(r"C:\Users\aadi\Desktop\python_full\Project\path_define" ,
               r"C:\Users\aadi\Desktop\python_full\Project\path_define\\2.txt" ,".mp4")




