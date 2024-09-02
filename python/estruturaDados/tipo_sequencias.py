# SEQUENCIA SIMPLES
'''
Armazenam itens de um unico tipo de dado
Cada item é armazenado em seu próprio espaço de memória
'''

aluno = 'Gabriel'


# SEQUENCIA CONTAINER

'''
Podem armazenar itens de diferentes tipos

Não armazenam o valor de seus itens em si, mas em suas 
referencias
'''

lista_aluno =['G', 25, 1.83]



# SEQUENCIAS MUTAVEIS

'''
Se refere a sequencias que podem ser alteradas após sua criação

exemplos: list - dict
'''

lista_letras = ['A','B','C']
print(lista_letras)

#.append adiciona o valor em () a variavel lista_letras
lista_letras.append('D')
print(lista_letras)


# SEQUENCIAS IMUTAVEIS

'''
Se refere a sequencias que NÃO podem ser alteradas após sua criação

exemplos: str - tuple - frozenset
'''

nome = 'Gabriel'
print(nome)
print(id(nome))

nome = 'Damas'
print(nome)
print(id(nome))

'''
Explicação: Quando alteramos o valor de uma variavel string ela não muda,
ao inves disso, se cria uma nova string e atribuindo a referencia dela a
variavel nome.
'''