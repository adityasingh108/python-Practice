import time 
from functools import lru_cache

@lru_cache(maxsize=5)
def Some_work(n):
    time.sleep(n)
    print(time.time())
    return n 


if  __name__ == "__main__":
    print("doing some work ")
    Some_work(2)
    Some_work(3)
    print('doing again')
    Some_work(5)