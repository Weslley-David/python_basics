import os
def exemplo(num):#essa função apenas coleta  o número e adiciona +1
    num+=1
    print(num)
    os.system('pause')

numero = int(input('Insira um número: '))
try:
    exemplo(numero)#em caso de erro na função( como passar uma letra ao invés de um número) o bloco except será executado.
except:
    print('Argumento inálido.')
    os.system('pause')
