import random, time

numeros = []
apoio = 0
todososjogos = []
jogo = []
jogadas = 1

print('-'*40)
print(f'{"JOGO DA MEGA SENA":^40}')
print('-'*40)


while True:
    jogo.append(int(input(f'Digite a {jogadas}º jodada: ')))
    jogadas += 1
    if jogadas >= 7:
        break


qtd = int(input('Quantos jogos quer sortear? '))
print('-='*4, f' SORTEANDO {qtd} JOGOS ', '=-'*4)

for x in range(0, qtd):
    while len(numeros) < 6:
        apoio = random.randint(1, 60)

        if apoio not in numeros:
            numeros.append(apoio)
            todososjogos.append(apoio)

    jogo.sort()
    numeros.sort()
    print(f'Jogo {x+1}: {numeros}')
    if jogo == numeros:
        print('ACERTOU!!!')
        exit(0)

    numeros.clear()
    #time.sleep(0.5)

print('-='*4, f'{"BOA SORTE":^18}', '-='*4)
print(f'O que voce jogou: {jogo}')

resultadofinal = []
dicionario = []
#print(todososjogos)

for z in range(1,61):
    dicionario.append([todososjogos.count(z), z])


dicionario.sort(reverse=True)
#print(dicionario)
for a, b in enumerate(dicionario):
    print(f'Numero {b[1]} foi sorteado: {b[0]}')
    if a == 9:
        break
