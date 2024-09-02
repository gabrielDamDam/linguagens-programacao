'''
Conjunto é uma coleção não ordenada e não indexada de elementos unicos.

Os conjuntos são delimitados por chaves {} em sua sintaxe

Não permitem valores duplicados
'''

frutas = {'banana','uva','goiaba'}
print(frutas)
print(type(frutas))

frutas.add('carambola')
print(frutas)

frutas.remove('carambola')
print(frutas)

print('-------------------------------------------------------')

'''
Para criar um conjunto vazio, é necessario usar set()
'''

dados = {}
print(type(dados))

dados2 = set()
print(type(dados2))

print('-------------------------------------------------------')

'''
Os conjuntos (sets) são uteis para testes de associação, eliminação
de entradas duplicadas, e realização de operações matemáticas (união,
intersecção, diferença e diferença simétrica)
'''

animal1 = set('cavalo')
animal2 = set('cachorro')
#lembrar que um set não permite elementos duplicados
print(animal1)
print(animal2)

#EXEMPLO DE DIFERENÇA
print(animal1.difference(animal2))

#EXEMPLO DE UNIÃO
print(animal1.union(animal2))

#EXEMPLO DE INTERSECÇÃO
print(animal1.intersection(animal2))

#EXEMPLO DE DIFERENÇA SIMÉTRICA
print(animal1.symmetric_difference(animal2))