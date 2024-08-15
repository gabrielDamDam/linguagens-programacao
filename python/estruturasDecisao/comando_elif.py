# ELSE IF

idade = 25
palpite = int(input('Descubra a minha idade:'))

if (palpite == idade):
    print('Acertou')
elif (palpite < idade):
    print('Errou para menos')
elif (palpite > idade):
    print('Errou para mais')