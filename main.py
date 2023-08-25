import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
from statsmodels.tsa.holtwinters import SimpleExpSmoothing

#CARREGANDO DADOS
data_frame = pd.read_csv('dataset.csv')
'''print(data_frame.shape)#Shape do data frame
print(data_frame.columns)#Colunas do data frame
print(data_frame.head())#Primeiros registros
print(data_frame.tail())#Utlimos registros'''

#PRÉ-PROCESSAMENTO DE DADOS
'''print(data_frame['Data'].min())
print(data_frame['Data'].max())'''
#Para análisar seríes temporais a coluna de data deve ser tratada como um índice da série e não como uma coluna individual
data_frame['Data'] = pd.to_datetime(data_frame['Data'])#Convertendo para datetime

#Converter o DataFrame em uma série temporal com a data como índice
serie_temporal = data_frame.set_index('Data')['Total_Vendas']
print(type(serie_temporal))

serie_temporal = serie_temporal.asfreq('D')
print(serie_temporal)

#ANÁLISE EXPLORATÓRIA
#Criar o gráfico da série temporal (sem formatação)
'''plt.figure(figsize=(12,6))
plt.plot(serie_temporal)
plt.xlabel('Data')
plt.ylabel('Vendas')
plt.title('Série Temporal de Vendas')
plt.grid(True)
plt.show()'''

#Criar o gráfico da série temporal (Com formatação)

#Criar o gráfico da série temporal com layout de contraste
plt.figure(figsize=(12,6))
plt.plot(serie_temporal,color ='white', linewidth = 2)

#Configurar cores e estilo do grafico
plt.gca().set_facecolor('#2e03a3')
plt.grid(color = 'yellow', linestyle = '--', linewidth = 0.5)

#Configurar  rótulo dos eixos, título e legenda
plt.xlabel('Data', color = 'black',fontsize = 14)
plt.ylabel('Vendas', color='black',fontsize=14)
plt.title('Série Temporal De Vendas',color='black', fontsize = 18)

#Configurar as cores dos eixos e dos tick (marcadores)
plt.tick_params(axis='x', colors = 'black')
plt.tick_params(axis='y',colors ='black')
plt.show()
