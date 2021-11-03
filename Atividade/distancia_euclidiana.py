#distância Euclidiana
import os
import math
renda = [9.6, 8.4 ,2.4 ,18.2 ,3.9 ,6.4]
idade = [28, 31, 42, 38, 25, 41]
#a=0 , f=5

def distancia_euc(rend, idad):
        x = 0
        dist_euc = 0.0
        while x < 6:
                dist_euc = math.pow(math.pow(rend - renda[x],2) + math.pow(idad - idade[x],2), 0.5)#distancia euclidiana
                file.write(str(dist_euc)+ '\n')
                print(dist_euc)
                x = x + 1
        #file.write('\n')

i = 0
file = open('distancia_euclidiana.txt', 'w+')
while i < 6:
        print(i)
        #file.write(str(i + 1)+ '=============\n')
        distancia_euc(renda[i], idade[i])
        i = i + 1

file.close()
