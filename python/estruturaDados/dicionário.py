'''
Dicionário é uma estrutura de dados que armazena elementos de forma não ordenada.

São compostos por pares de chave-valor, cada elementos é identificado por uma chave única

Os ITENS de um dicionário são ordenados, mutáveis e não permitem valores duplicados
'''

dados = {'Nome':'Gabriel','Idade':'25',
         'Cidade':'Diadema'}

print(dados)
print(type(dados))


print('----------------------------------------------------------')

'''
Dicionário é o equivalente a Matriz em JAVA

A principal vantagem dos dicionários é a capacidade de acessar os elementos de forma
eficiente, fornecendo uma chave que identifica de maneira única o valor desejado.
Isso torna mais fácil e intuitivo recuperar e manipular dados com base em critérios especificos

Dicionários são delimitados por chaves {}
Chaves são delimitadas por aspas simples ('chave':'valor')
Os valores associados às chaves podem ser de qualquer tipo válido
'''

identificacao = {'Nome':'Gabriel','Idade':'25',
         'Cidade':'Diadema'}

#Os elementos de um dicionário são acessados por suas chaves ou valores

print(identificacao['Nome'])
print(identificacao['Idade'])

print('----------------------------------------------------------')

#Dicionarios possuem um metodo chamado keys() que devolve o conjunto de suas chaves

print(identificacao.keys())

#Dicionarios possuem um metodo chamado values() que devolve os valores

print(identificacao.values())

print('----------------------------------------------------------')

'''
Outra forma de se criar um dicionário é usando a função dict()
'''

identificacao2 = dict(Nome='Igor', Idade='25', Cidade='Sao Bernardo')
print(identificacao2)