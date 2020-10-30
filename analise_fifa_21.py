#!/usr/bin/env python
# coding: utf-8

# In[278]:


import pandas as pd
import seaborn as srn
import statistics  as sts
import numpy as np
import matplotlib.pyplot as plt


# In[279]:


# Consultando dados Fifa 21
fonte = "C://Fifa 21//fifa21.csv"

# Leitura do arquivo e criando DataFrame
df = pd.read_csv(fonte, sep=';')

# Visualizando DataFrame
df.head()


# In[280]:


df.shape


# In[281]:


df.columns = ["ID_JOGADOR", "NOME", "NACIONALIDADE", "POSICAO", "OVERALL", "IDADE", "HITS", "POTENCIAL", "CLUBE"]


# In[282]:


df.head()


# In[283]:


# Verificando dados nulos
df.isnull().sum()


# In[284]:


# Verificando tipo de dados das colunas
df.dtypes


# In[286]:


# criando um DataFrame para separar o campo "POSICAO"
trata_posicao = lambda x: pd.Series([i for i in x.split('|')])
pos = df['POSICAO'].apply(trata_posicao)

# renomeando a coluna de acordo com seu indice
df['POSICAO_01']=pos[0]
df['POSICAO_02']=pos[1]
df['POSICAO_03']=pos[2]
df['POSICAO_04']=pos[3]
df['POSICAO_05']=pos[4]

df.head(5)


# In[463]:


df.drop('POSICAO', axis=1)


# In[288]:


# Quantidade total de nacionalidades retirando duplicatas
df["NACIONALIDADE"].nunique()


# In[289]:


# Quantidade total de jogadores por nacionalidade
df["NACIONALIDADE"].value_counts()


# In[487]:


plt.style.use('ggplot') #top 50 nations that the players represent in FIFA 2021
plt.figure(figsize = (20,10))
df['NACIONALIDADE'].value_counts().head(10).plot.bar(color = '#121619', fontsize = 'large')
plt.title('Jogadores x País')
plt.xlabel('País', fontsize = 'xx-large', color = '#121619')
plt.ylabel('Quantidade', fontsize = 'xx-large', color = '#121619')
plt.show()


# In[290]:


# Quantidade total de jogadores por nacionalidade (2ª opcao ordem alfabetica)
agrupado_nacionalidade = df.groupby(['NACIONALIDADE']).size()
agrupado_nacionalidade


# In[ ]:


# idade


# In[464]:


df["OVERALL"].hist(bins = 20, figsize=(8,6))


# In[465]:


# Quantidade de posições diferentes incluindo jogadores polivalentes (combinação)
df["POSICAO"].nunique()


# In[488]:


# Quantidade de jogadores por posição
df["POSICAO"].value_counts()


# In[293]:


df["POSICAO_01"].nunique() # quantidade de posições distintas no jogo


# In[294]:


# Quantidade de jogadores por posição 01 (principal) distinta
df["POSICAO_01"].value_counts()


# In[296]:


# Melhores jogadores do jogo
df[["POSICAO_01", "POSICAO_02", "NOME", "OVERALL", "CLUBE"]].head(10)


# In[466]:


# Visualizando Centro Avante (Striker)
atacantes = df.loc[(df['POSICAO_01'] == 'ST')
       | (df['POSICAO_02'] == 'ST')
       | (df['POSICAO_03'] == 'ST')
       | (df['POSICAO_04'] == 'ST') 
       | (df['POSICAO_05'] == 'ST')]

atacantes["OVERALL"].hist(bins = 20, figsize=(8,6))


# In[299]:


atacantes["POTENCIAL"].hist(bins = 20, figsize=(8,6))


# In[338]:


# Função para OVERALL
def player_top_overall(posicao, qtd = 10):
    pos = df.loc[(df['POSICAO_01'] == posicao) 
                       | (df['POSICAO_02'] == posicao)
                       | (df['POSICAO_03'] == posicao)
                       | (df['POSICAO_04'] == posicao) 
                       | (df['POSICAO_05'] == posicao)]
    return pos.nlargest(qtd, "OVERALL")[["POSICAO_01", "NOME", "OVERALL", "POTENCIAL", "CLUBE"]]

def player_bottom_overall(posicao, qtd = 10):
    pos = df.loc[(df['POSICAO_01'] == posicao) 
                       | (df['POSICAO_02'] == posicao)
                       | (df['POSICAO_03'] == posicao)
                       | (df['POSICAO_04'] == posicao) 
                       | (df['POSICAO_05'] == posicao)]
    return pos.nsmallest(qtd, "OVERALL")[["POSICAO_01", "NOME", "OVERALL", "POTENCIAL", "CLUBE"]]

# Função para POTENCIAL
def player_top_potencial(posicao, qtd = 10):
    pos = df.loc[(df['POSICAO_01'] == posicao) 
                       | (df['POSICAO_02'] == posicao)
                       | (df['POSICAO_03'] == posicao)
                       | (df['POSICAO_04'] == posicao) 
                       | (df['POSICAO_05'] == posicao)]
    return pos.nlargest(qtd, "POTENCIAL")[["POSICAO_01", "NOME", "OVERALL", "POTENCIAL", "CLUBE"]]

def player_bottom_potencial(posicao, qtd = 10):
    pos = df.loc[(df['POSICAO_01'] == posicao) 
                       | (df['POSICAO_02'] == posicao)
                       | (df['POSICAO_03'] == posicao)
                       | (df['POSICAO_04'] == posicao) 
                       | (df['POSICAO_05'] == posicao)]
    return pos.nsmallest(qtd, "POTENCIAL")[["POSICAO_01", "NOME", "OVERALL", "POTENCIAL", "CLUBE"]]

# Função para jogador
def pesquisa_jogador(nome_jogador):
    return df.loc[(df['NOME'] == nome_jogador)]


def pesquisa_plantel(nome_clube):
    return df.loc[(df['CLUBE'] == nome_clube)]


# In[489]:


# Melhores jogadores (posicao por parametro, qtd)
player_top_overall("ST")


# In[490]:


# Piores jogadores (posicao por parametro, qtd)
player_bottom_overall("ST")


# In[493]:


# Melhores potenciais (posicao por parametro, qtd)
player_top_potencial("ST")


# In[492]:


# Piores potenciais (posicao por parametro, qtd)
player_bottom_potencial("ST")


# In[518]:


def pesquisa_plantel(club): 
    return df[df['CLUBE'] == club][['NOME','OVERALL','POTENCIAL','POSICAO','HITS','IDADE']]


# In[521]:


pesquisa_plantel('Nome')


# In[523]:


plt.figure(figsize=(8,6))
srn.lineplot(df['OVERALL'], df['IDADE'], color = '#121619')
plt.title('Overall x Idade', fontsize = 14)
plt.show()

