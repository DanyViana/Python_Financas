# Para importar a bibliote math, que será utilizada em cálculos matemáticos, você pode realizar de algumas formas: 

#Forma mais comum é importando toda a biblioteca: 
import math 
raiz = math.sqrt(16) #O nome do módulo e o nome da função, nesse caso é o sqrt (raíz quadrada)
print (raiz)

#Se você souber que vai utilizar apenas a raíz quadrada, é possível fazer somente dessa forma: 
from math import sqrt
raiz2 = sqrt(25)
print (raiz2)

#A que os especilistas mais gostam e é utilizada em códigos mais complexos pois economiza palavras são essas duas formas:
from math import sqrt as s
raiz3a = s(36)
print (raiz3a)

import math as m
raiz3b = m.sqrt(49)
print (raiz3b)

#A última é muito desaprovada por especialistas:
from math import * #Vai importar tudo da biblioteca math
raiz4 = sqrt(64)
print (raiz4)
#Essa opção pode ser problemática principalmente se você importar outros módulos que tenham a mesma função que você está trabalhando, o python irá escolher a que ele quiser. 

#Biblioteca "numpy" é um pacote de terceiros que nos permite trabalhar com arrays (organizar e processar dados) multidimensionais. 

#Biblioteca "pandas" nos permite organizar os dados em uma forma tabular e anexar rótulos descritivos as linhas e colunas da tabela. Ótimo para trabalhar com séries temporais e banco de dados enormes. 

#Biblioteca "matplotlib" é de gráficos bidimensionais especialmente projetada para visualização de cálculos numpay.

#Biblioteca "math" para funções matemáticas.

#Biblioteca "random" é para gerar números aleatórios.

#Biblioteca "statsmodels" é para estatística descritiva e plotagem de gráficos.

#Todas essas bibliotecas já estão instaladas no pacote do Anaconda.

#Para instalar alguma biblioteca é só ir no menu inicial, procurar por "anaconda prompt", digite "pip install (nome da biblioteca)" - pip install pandas_datareader e apertar enter. Prontinho! 