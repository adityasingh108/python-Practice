try:
    n = int(input("Enter The Number Harry ha got:")) # 
    mn = int(input("What is the minum Number:"))
    mx = int(input("What is the maximum :"))
except:
    print("Enter Intinger only")
    exit()
if mx<mn: # if minimam length of of is greater than the maximum length 
    print("Maximum number is not lesser than the minum number")
    exit()        
for i in range(mn,mx+1):#lopping start
    if n%i==0: # if n is divide by minimum number
        print(f"{i} is divisible by {n}")
    if n%i!=0:
        print(f"{i} is not Divisible by {n}")