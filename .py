def jogar():

    import random

    print('################################')
    print('Bem vindo ao Jogo de adivinhação')
    print('################################')
    print()
    numero_secreto = round(random.randrange(1,101)) # gera um número a partir do range
    rodada = 1
    print('Escolha o nível do seu jogo: \n 1- Fácil \n 2- Médio \n 3- Difícil')
    nivel = int(input('Informe o nível escolhido:'))
    total_tentativas = 0

    if (nivel == 1):
        total_tentativas = 10
    elif (nivel == 2):
        total_tentativas = 5
    else:
        total_tentativas = 3

    for rodada in range (1,total_tentativas + 1 ):

        '''adicionamos mais 1 pois o stop não é inclusivo, ou seja se for 3 ele irá repetir até o 2 '''

        print('Tentativa {} de {}'.format(rodada,total_tentativas))
        chute = int(input('Digite um valor:'))

        if (chute < 1 or chute > 100):
            print('Número inválido, digite um número que seja Maior que 1 e Menor que 100')
            continue

        maior = chute > numero_secreto
        acertou = chute == numero_secreto
        menor = chute < numero_secreto
        if (acertou):
            print('Você acertou o número secreto !!!')
            break
        elif (maior):
            print('Você errou o número, você digitou um número maior')
        elif (menor):
            print('Você errou o número, você digitou um número menor')
if (__name__ == "__main__"):
    '''name é o nome do arquivo e main o nome do arquivo que estará rodando'''
    jogar()
