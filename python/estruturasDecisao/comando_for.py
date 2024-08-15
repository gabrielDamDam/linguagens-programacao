''''

for i in range(0,10):
    print(i)

print('----------------')

for j in range(1,10,3):
    print(j)

print('----------------')

'''

idade = 25
tentativas = 5

for rodada in range (1,tentativas + 1):
    print('Iniciando rodada {}'.format(rodada))

    palpite = int(input('Descubra a minha idade:'))
    acertou = palpite == idade
    maior = palpite > idade
    menor = palpite < idade

    if (acertou):
        print('ACERTOU')
        break
    elif (maior):
        print('ERROU! A idade é menor')
    elif (menor):
        print('ERROU! A idade é maior')

    if rodada == 5:
        print('Voce perdeu')
        break