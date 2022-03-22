import random

probabilidade = random.random() #Gera um float aleatório no intervalo [0;1)
print(probabilidade)

numero_dado = random.randint(1,6) #Randomiza em um intervalo fornecido (nesse caso entre 1 e 6 que são os números de um dado) e fornece um valor inteiro.
print (numero_dado)
 
import numpy as np #Chamando a biblioteca para trabalhar com o array

matriz_aleatoria = np.random.randint(1,6,(4,6)) #O mesmo raciocínio anterior, mas com a indicação do número de linhas e colunas da matriz, nesse caso foi uma matriz de 4 linhas com 6 colunas. 
print(matriz_aleatoria)