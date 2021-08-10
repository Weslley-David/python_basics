import os
# tipos de variáveis
num_1 = 7       #Inteiro
num_2 = 1.0     #Float
num_3 = 4+3j    #Complex
a = True;       #Boolean
string = 'oie'  #Strings
vetor = ['olá', 7, True]#Vetores
dicionario = {'User':'root', 'password': 12345}

#output de variáveis
print('numero inteiro     : ',num_1)
print('numero float       : ',num_2)
print('numero complexo    : ',num_3)
print('proposição booleana: ',a)
print('strings            : ',string)
print('vetor              : ',vetor)
print('vetor com índice   : ',vetor[2])
print(dicionario['password'])

print(type(num_1))#type retorna o tipo de uma variável
os.system('pause')
