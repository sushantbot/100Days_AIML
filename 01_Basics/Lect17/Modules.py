import math

# Some functions inside math library/module
print(math.factorial(5))
print(math.floor(6.9))
print(math.ceil(6.9))
print(math.sqrt(100))
print(math.pow(2,3))
print(math.pi)
print(math.e)


import time

print("time.time:",time.time())
print("time.ctime:",time.ctime())

print("hello")
time.sleep(1)
print("World")  # prints world after 5 seconds of printing of hello


import os
print(os.getcwd())  #prints current working directory
print(os.listdir()) #prints the directories in current directory
