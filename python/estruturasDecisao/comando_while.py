idade = 25
tentativas = 5
rodada = 1
perdeu = True

while (tentativas > 0):
    print('Iniciando rodada {}! Voce tem mais '
          '{} tentativas'.format(rodada, tentativas))

    palpite = int(input('Descubra a minha idade:'))
    acertou = palpite == idade
    maior = palpite > idade
    menor = palpite < idade

    if (acertou):
        print('ACERTOU')
        perdeu = False
        break;
    elif (maior):
        print('ERROU! A idade é menor')
    elif (menor):
        print('ERROU! A idade é maior')

    tentativas = tentativas - 1
    rodada = rodada + 1


    if (perdeu and tentativas == 0):
        print('Voce Perdeu!')