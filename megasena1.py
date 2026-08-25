import random
import os
os.system('cls')
contador = 0
while contador <=9:
    numeros = random.sample(range(1,25),15)
    contador +=1
    numeros.sort(reverse=False)
    print (numeros)
    if (22 in numeros and 22 in numeros and 12 in numeros):
        print('acertou')
    else:
        print('errou')
