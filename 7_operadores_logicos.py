import os
# Or, and, not
# Utilizados para operar valores booleanos e assim executar ações
var_false = False
var_true = True

resultado = (var_false or var_true) #True
print(resultado)
resultado_2 = (var_false and var_true) #False
print(resultado_2)
resultado_3 = (not(var_false) and var_true) #True
print(resultado_3)
os.system('pause')

#operadores de identidade
#operadores de associação