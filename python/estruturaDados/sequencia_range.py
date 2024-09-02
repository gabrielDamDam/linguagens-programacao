'''
Range é um tipo de sequencia de numeros, comumente usado para
fazer iterações em um comando For, representando um valor especifico
de valores.

Ele gera uma sequencia de numeros especificando o valor de inicio,
fim e o passo de incremento.

range(inicio, total de itens)
'''

for sequencia in range (1, 5):
    print(sequencia)

print('-----------------------------------')


for sequencia2 in range(0,10,2):
    print(sequencia2)


'''
O range não imprime os elementos de uma sequencia, ele armazena e
imprime a ordem de inicio e o final do intervalo especificado.

Para imprimir os elementos da sequencia, é necessario utilizar um laço
For em conjunto com o range
'''


# EXEMPLO DE APLICAÇÃO

tabuada = int(input('Qual tabuada deseja consultar?:'))
for i in range(1, 11):
    print("{} * {} = {}".format(tabuada,i,(i*tabuada)))


