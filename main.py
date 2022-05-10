'''Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando o laço for.'''
num = int(input('Digite o número desejado para a tabuada: \n'))
for cont in range (1,11):
  print(f'{num} X {cont} = {num*cont}')