import random

print('Jogo de Operações Matematicas')
while True:
    aletorio = random.randrange(1,6)
    if aletorio == 1:
        a = random.randrange(1,12)
        b = random.randrange(1,12)
        print(f'{a} + {b}')
        resposta = int(input('Digite a resposta da operação: '))
        if resposta == a+b:
            print(f'Você acertou a resposta')
        else:
            print(f'Você errou a resposta correta é {a+b}')
            break

    if aletorio == 2:
        a = random.randrange(1,12)
        b = random.randrange(1,12)
        print(f'{a} - {b}')
        resposta = int(input('Digite a resposta da operação: '))
        if resposta == a-b:
            print('Você acertou a resposta')
        else:
            print(f'Você errou, a resposta correta é {a-b}')
            break

    if aletorio == 3:
        a = random.randrange(1,12)
        b = random.randrange(1,12)
        print(f'{a} x {b}')
        resposta = int(input('Digite a resposta da operação: '))
        if resposta == a*b:
            print('Você acertou a resposta')
        else:
            print(f'Você errou, a resposta correta é {a*b}')
            break

    if aletorio == 4:
        a = random.randrange(1,12)
        b = random.randrange(1,12)
        print(f'{a} / {b}')
        resposta = int(input('Digite a resposta da operação: '))
        if resposta == a/b:
            print('Você acertou a resposta')
        else:
            print(f'Você errou, a resposta correta é {a/b}')
            break

    if aletorio == 5:
        a = random.randrange(1,12)
        b = random.randrange(1,12)
        print(f'{a} ^ {b}')
        resposta = int(input('Digite a resposta da operação: '))
        if resposta == a**b:
            print('Você acertou a resposta')
        else:
            print(f'Você errou, a resposta correta é {a**b}')
            break

    if aletorio == 6:
        a = random.randrange(1,12)
        print(f'Qual é raiz quadrada de {a}')
        resposta = int(input('Digite a resposta da operação: '))
        if resposta == a**(1/2):
            print('Você acertou a resposta')
        else:
            print(f'Você errou, a resposta correta é {a**(1/2)}')
            break



