#https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbUtoM25lSkprYzJlNVkzaFA4WUxqMU9hWGVLd3xBQ3Jtc0ttdmJJcWFlMUdFOW8yWGhYbzRKaFB4ZFJ4eFppdW0zREZoVFUxLVB2WG9HWHRtVFJ4T04yRlBnVFpQeTVfQ2hNSEx2VnNjSEx4SGhFamN6d05qR0VyS2Z3Zk01QUpZVmdPbWUtTU8zSmxkRll0QmlQMA&q=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ffunctions.html%23open
import os
#'r'    #open for reading (default)
#'w'    #open for writing, truncating the file first
#'x'    #open for exclusive creation, failing if the file already exists
#'a'    #open for writing, appending to the end of the file if it exists
#'b'    #binary mode
#'t'    #text mode (default)
#'+'    #open for updating (reading and writing)

file = open('arquivo.txt', 'w+')#w+ serve para ler e escrever arquivos
file.write('linha 1\nlinha 2\n')#método para escrever no arquivo
file.write('linha 3\n')
file.seek(0, 0) # retona o cursor ao início do arquivo
print(file.read())# lê o arquivo

print('==========')
file.seek(0,0)
print(file.readline())#lê apenas uma linha
print(file.readline())
print(file.readline())

file.seek(0, 0)
for linha in file:
    print(linha, end = '')
file.close()#função para fechar o arquivo
os.remove('nome_do_arquivo.txt')# apagar arquivo
os.system('pause')