''''
ATIVIDADE 1

Criar um script que capture o nome, a idade e exiba
na tela, sendo uma linha para cada dado
'''

nome = input("informe seu nome completo: ")
idade = input("ïnforme sua idade(apenas numero): ")

# CONCATENAÇÃO
mensagem1 = 'Seu nome é ' + nome + ' e sua idade é ' + idade

# INTERPOLAÇÃO
mensagem2 = 'Seu nome é {} e sua idade é {}'.format(nome, idade)

print(mensagem1)
print(mensagem2)