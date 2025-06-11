import random

acertos = 0
erros = 0

lista_raiz = [4,9,16,25,36,49,64,81]

while True:
    
    if erros == 3:
        print('Você perdeu')
        print(f'Você acertou {acertos} e errou {erros}')
        break
    
    aletorio = random.randrange(1,6)

    if aletorio == 0:
        a = random.randrange(1,12)
        b = random.randrange(1,6)
        print(f'{a} + {b}')
        resposta = float(input('Digite a resposta: '))
        if resposta == a+b:
            print('Parabens você acertou')
            acertos += 1
        elif resposta != a+b:
            print(f'Você errou, a resposta correta é {a+b}')
            erros += 1
    
    elif aletorio == 1:
        a = random.randrange(1,12)
        b = random.randrange(1,6)
        print(f'{a} - {b}')
        resposta = float(input('Digite a resposta: '))
        if resposta == a-b:
            print('Parabens você acertou')
            acertos += 1
        else:
             print(f'Você errou, a resposta correta é {a-b}')
             erros += 1
    
    elif aletorio == 2:
         a = random.randrange(1,12)
         b = random.randrange(1,6)
         print(f'{a} x {b}')
         resposta = float(input('Digite a resposta: '))
         if resposta == a*b:
              print('Parabens você acertou')
              acertos += 1
         else:
             print(f'Você errou, a resposta correta é {a*b}')
             erros += 1
    
    elif aletorio == 3:
        a = random.randrange(1,12)
        b = random.randrange(1,6)
        print(f'{a} / {b}')
        resposta = float(input('Digite a resposta: '))
        if resposta == a/b:
            print('Parabens você acertou')
            acertos += 1
        else:
             print(f'Você errou, a resposta correta é {a/b}')
             erros += 1
    
    elif aletorio == 4:
        a = random.randrange(1,12)
        b = random.randrange(1,4)
        print(f'{a} ^ {b}')
        resposta = float(input('Digite a resposta: '))
        if resposta == a**b:
            print('Parabens você acertou')
            acertos += 1
        else:
             print(f'Você errou, a resposta correta é {a**b}')
             erros += 1
    
    elif aletorio == 5:
        a = random.choice(lista_raiz)
        print(f'Qual a raiz quadrada de {a}')
        resposta = float(input('Digite a resposta: '))
        if resposta == a**(1/2):
            print('Parabens você acertou')
            acertos += 1
        else:
             print(f'Você errou, a resposta correta é {a**(1/2)}')
             erros += 1
    




    