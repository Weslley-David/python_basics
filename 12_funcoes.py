import os
num = float(input('teste o input: '))
def impar_ou_par(numero):
    if(numero % 2 == 1):#Se a consição é satisfeita, executa-se as ações presentes nesse bloco.
        print(numero, 'é impar')
    elif(numero == 0):
        print('0 é par')#é possível adicionar diferentes proposições, nesse caso, se a proposição acima for verdadeira, esta não é executada.
    else:
        print(numero, 'é par')#caso todas as ações resultem em valor falso, essa ação é executada.

num = impar_ou_par(num) #lembrar de declarar a função antes de usá-la klklklkjkkjk
os.system('pause')