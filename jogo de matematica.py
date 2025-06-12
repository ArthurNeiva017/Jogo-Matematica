import random

# Contagem de acertos e erros 
acertos = 0
erros = 0
    
#Lista de Raizes que são de números inteiros
lista_raiz = [4,9,16,25,36,49,64,81]


while True:
    
    # Se o usuário errou 3 vezes, o programa acaba
    if erros == 3:
        print('Você perdeu')
        print(f'Você acertou {acertos} e errou {erros}')
        break
    
    # O programa vai selecionar aleatoriamente algumas das operções
    aletorio = random.randrange(1,6)

    #Operação de Adição com  números aletorios
    if aletorio == 0:
        a = random.randrange(1,12)
        b = random.randrange(1,6)
        print(f'{a} + {b}')
        resposta = float(input('Digite a resposta: '))
        if resposta == a+b:
            print('Parabens você acertou')
            acertos += 1
        else:
            print(f'Você errou, a resposta correta é {a+b}')
            erros += 1
    
    #Operação de Subtração com  números aletorios
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
    
    #Operação de Multiplicação com  números aletorios
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
    
    #Operação de Divisão com  números aletorios
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
    
    #Operação de Potenciação com  números aletorios
    elif aletorio == 4:
        a = random.randrange(1,12)
        b = random.randrange(1,3)
        print(f'{a} ^ {b}')
        resposta = float(input('Digite a resposta: '))
        if resposta == a**b:
            print('Parabens você acertou')
            acertos += 1
        else:
             print(f'Você errou, a resposta correta é {a**b}')
             erros += 1
    
    #Operação de Raiz Quadrada com  números aletorios
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
    

    '''
    Proxima fase do desenvolvimento do jogo é ter no minímo 3 níveis de dificuldade

    '''




    