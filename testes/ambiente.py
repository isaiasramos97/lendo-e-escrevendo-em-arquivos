import os

print(os.path.join('usr', 'bin', 'spam'))
# linux ou OS X: retorna 'usr/bin/spam'. no caso do windows: 'usr\\bin\\spam'
# esta função é útil se houver necessidade de criar strings para os nomes de arquivos
# o ex a seguir une os nomes de uma lista de nomes de arquivo no final do nome de uma pasta:

my_files = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in my_files:
    print(os.path.join('/Users/asweigart', filename))

# diretorio de trabalho atual

os.getcwd()  # retorna o diretorio de trabalho atual
# os.chdir('/Users/Documents/Projects')   # colocando o path como uma string entre os parenteses, altera-se o diretório

# o programa pode criar novas pastas (diretorios) com a função osmakedirs()
# o comando criará as pastas delicious, walnut, waffles em cadeia
'''
os.makedirs('../candy')  # dois pontos: na pasta pai
os.makedirs('./delicious/walnut/waffles')   # um ponto: na pasta atual
'''
# os códigos acima foram comentados para não rodarem nos próximos testes

# lidando com paths absolutos e relativos

# chamar os.path.abspath(path) retornará uma string com o path absoluto referente ao argumento
print(os.path.abspath('.'))

# para verificar se um dado path representa um path absoluto
print(os.path.isabs('/home/username/Documentos/MyProjects/lendo-e-escrevendo-em-arquivos/testes'))  # True or False

