'''
Desenvolver o jogo da forca, aplicando os conhecimentos como
estruturas de decisão, listas, conjuntos e loops.
'''


def jogar():
    letras_usadas = set()  # Conjunto para armazenar as letras que já foram chutadas
    palavra_secreta = input("Digite a palavra para ser descoberta: ")
    print("\n" * 100)  # Limpa a tela para ocultar a palavra secreta
    print('*********************************')
    print('***Bem-vindo ao jogo da Forca!***')
    print('*********************************')

    letras_acertadas = ["_"] * len(palavra_secreta)  # Inicializa a lista de letras acertadas com "_" no tamanho da palavra
    enforcou = False
    acertou = False
    erros = 0

    print(' '.join(letras_acertadas))  # Mostra as letras acertadas (inicialmente tudo "_")

    while not enforcou and not acertou:
        chute = input("Digite uma letra: ").upper()

        if chute in palavra_secreta.upper():
            for posicao, letra in enumerate(palavra_secreta.upper()):  # Itera sobre cada letra da palavra com seu índice
                if chute == letra: letras_acertadas[posicao] = letra  # Se a letra chutada estiver na palavra, substitui o "_" pela letra correta na posição correspondente

            print(' '.join(letras_acertadas))
        else:
            erros += 1
            print(f"Você errou! Você ainda tem {6 - erros} tentativas.")

        letras_usadas.add(chute)
        print("Letras usadas: {}".format(letras_usadas))

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas  # Define "acertou" como True se não houver mais "_" na lista de letras acertadas

    if acertou:
        print("Você ganhou!!")
    else:
        print("Você perdeu!!")

    print('Fim de jogo')

jogar()