import numpy as np
import pandas as pd

ser = pd.Series(np.random.random(5), name = 'coluna 1') #Séries é uma coluna de dados, um conjunto de informações relacionados a uma única variável. Uma variável do tipo séries com 5 números que foram criados de forma aleatória. É escolhido o nome da coluna. 
print(ser)
print(ser[2]) #Vai retornar o terceiro valor da coluna. 

from pandas_datareader import data as wb
#DataFrame é parecido com o tipo de dados Séries, mas com várias colunas.

B3 = wb.DataReader('B3SA3.SA', data_source = 'yahoo', start = '2022-3-1') #É necessário especificar o símbolo da ação em questão, nesse caso é da B3SA (B3SA3.SA) para as ações da B3. A fonte de dados é o Yahoo e é necessário especificar qual a data de início que será extratída. 
print(B3)

#A diferença entre a coluna Close e Adj Close é devido ao pagamento de dividendos aos acionistas e outras mudanças nos preços. 
#Sádado, domingos e feriados nacionais não possuem dados devido ao fechamento do mercado. São dados de apenas os dias de negociações. 

print(B3.info()) #Mostrar os dados examinados, você consegue verificar se não tem nenhum dado faltante, os tipode dados. 

print(B3.head()) #Checkar as primeiras 5 linhas da base de dados. 
print(B3.tail()) #Checkar as últimas 5 linhas da base de dados. 
#Se quiser especificar um número maior de linhas, é só informar entre os parênteses o valor. 

#Para conseguir os dados de mais empresas podemos fazer da seguinte forma. As empresas serão: Procter&Gamble, Microsoft, AT&T, Ford, General Electric. Para os dados de Adj close (fechamento ajustado). 

tickers = ['PG', 'MSFT', 'T', 'F', 'GE'] #Criar uma lista com os símbolos das empresas que deseja pesquisar. 
new_data = pd.DataFrame() #Novo objeto com o panda
for t in tickers: #Para cada ticket em tickers
    new_data[t] = wb.DataReader(t, data_source = 'yahoo', start = '2022-3-1')['Adj Close'] #Me forneça o preço de fechamento ajustado para cada ticker (para cada instância) para cada dia desde 1/3/22. No final indicar o nome exato da coluna que queremos. 

print(new_data)

#Outras fontes para retirar os dados no lugar o Yahoo: 'morningstar' ou 'iex'. Atenção as datas e aos nomes dos campos, pois cada fornecedor (API) tem uma diferença. 

#Lembre-se que o python é case sensitive! Digite os nomes da coluna da mesma forma que é mostrado! 