ano_atual = 2024
aniversario = (int(input('informe o ano do seu aniversario: ')))
idade = ano_atual - aniversario
mensagem = ('Voce nasceu em {}, portanto tem {}'
            .format(aniversario, idade))

print(mensagem)