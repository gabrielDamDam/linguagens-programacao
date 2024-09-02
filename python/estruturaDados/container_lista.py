'''
LISTAS

sequencia ordenada
cada valor é identificado por um índice, começando do 0
podemos acessar e manipular os elementos da lista com base na sua posição

Listas podem conter elementos de diferentes tipos(string, int, boolean...)
Utilizar colchetes [] para criar listas, os elementos são separados por virgulas
'''

# CRIAÇÃO DA LISTA
minha_lista = [1,2,3,4]

#adicionar elemento a lista
minha_lista.append('cinco')
print(minha_lista[1])

#mostrar elemento da lista com base no índice (posição)
print(minha_lista[1])
print(minha_lista[4])
print(minha_lista[0])

print('--------------------------------')

#é possível passar valores negativos na consulta, isso faz com que retorne
#o valor de uma consulta reversa
print(minha_lista[-1])
print(minha_lista[-2])
print(minha_lista[-3])

print('--------------------------------')

# EXEMPLO DE APLICAÇÃO

''''

meses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho', 'Julho',
         'Agosto','Setembro','Outubro','Novembro','Dezembro']

mes = int(input('Informe o mes do seu aniversario (1 - 12): '))

#(meses[mes - 1]) = se faz dessa forma porque o código le a sua posição
# (indice) do elemento, por exemplo, Janeiro é o mes 1 mas
# está na posição 0.

print('Voce nasceu no mes de {}'.format(meses[mes - 1]))

'''

print('--------------------------------')


#EXEMPLO ELABORADO DO CÓDIGO ACIMA

'''

meses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho', 'Julho',
         'Agosto','Setembro','Outubro','Novembro','Dezembro']

quantidade_amigos = int(input('Quantos amigos voce tem?'))

#criação de uma lista vazia
camaradas = []

#criação do primeiro loop para identificar quantidade e nome dos camaradas
for i in range (0, quantidade_amigos):
    amigo = input('Digite o nome do seu amigo {}:'.format(str(i + 1)))
    camaradas.append(amigo)

for i in range (0, quantidade_amigos):
    mes_aniversario = int(input('Digite o mes do aniversario do seu amigo {}:'
                                .format(camaradas[i])))
    if 1 <= mes_aniversario < 13:
        print('{} nasceu no mes de {}'.format(camaradas[i], meses[mes_aniversario - 1]))
        
'''

# MANIPULAÇÃO DE MULTIPLOS VALORES DA LISTA, ATRAVÉS DE FATIAMENTO

meses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho', 'Julho',
         'Agosto','Setembro','Outubro','Novembro','Dezembro']

#Esse formato de busca (meses[X:Y] faz com que o código retorne todos os dados
#a partir de X e printe na tela tudo até chegar a posição Y).
print('O primeiro mes do ano é {}'.format(meses[:1]))
print('O primeiro Trimestre do ano é composto pelos meses{}'.format(meses[:3]))
print('O terceiro trimestre do ano é composto pelos meses{}'.format(meses[6:9]))
print('O primeiro semestre do ano é composto pelos meses{}'.format(meses[:6]))
print('O segundo semestre do ano é composto pelos meses{}'.format(meses[6:]))

print('--------------------------------')

# FUNCIONALIDADES PRONTAS

lista_numero = []
#a funcionaldiade .append permite adicionar apenas 1 dado por vez
lista_numero.append(1)
lista_numero.append('dois')

# a funcionalidade .extende permite adicionar mais de 1 dado por vez
lista_numero.extend([3,'quatro',2+3])
print(lista_numero)

#operadores também funcionam com listas
print(lista_numero*2)
