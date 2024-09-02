'''
Tupla é uma sequencia que não pode ser alterada após a sua criação.
Seus elementos não podem ser modificados, adicionados ou removidos
Se utiliza parenteses () como delimitadores
'''

exemplo_tupla = ('um','dois','tres','quatro')
print(type(exemplo_tupla))

'''
Podemos passar a funcao tuple() para criar uma tupla, passando
um objeto como argumento.
'''

numeros = (1,2,3,4)
tuple(numeros)
print(type(numeros))

print('-----------------------------------------------')

'''
Uma tupla é imutavel, mas é possivel criar uma tupla que contenha
objetos mutáveis, como listas. Isso significa que é possivel
modificar elementos dentro de uma tupla, mas a tupla permanece imutável
'''

lista = ['quatro','cinco']
exemplo_tupla2 = ('um','dois','tres', lista)
print(exemplo_tupla2)
lista.append('seis')
print(exemplo_tupla2)