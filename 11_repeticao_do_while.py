#Essa é uma tentativa de emular o comportamento do while de C++
import os
i = 1

while True:
    print(i)
    i = i + 1
    if(i > 3):
        break
os.system('pause')