# Array contém todos os elementos do mesmo tipo de dados (diferença entre as listas). 

import numpy as np
a = np.array([[0,1,2,3],[4,5,6,7]])
print(a)

#Organize os arrays com o mesmo número de elementos e sejam do mesmo tipo de dados 

print (a.shape) #Vai retornar a forma do array - indica que tem 2 linhas e 4 colunas (2,4)

print (a[1,3]) #Vai retornar o elemento dentro do array, lembre-se de começar pelo índice 0. 

a[1,2] = 8 #Para alterar um valor específico do array
print(a)

print(a[0]) #Vai mostrar a linha 0 do array
print(a[1])

#Um array unidimensional também é chamado de vetor. 
b = np.array([3,5])
print(b)

#Um array bidimensional também é chamado de matriz.