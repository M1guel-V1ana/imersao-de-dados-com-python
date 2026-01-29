import pandas as pd
import numpy as np


df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")
#observando os valores que estão faltantes na tabela, trazendo eles como falsos ou verdadeiros
print(df.isnull())
#exibir as 5 primeiras linhas da tabela
print(df.head())

# soma de todos os campos(valores) faltantes na tabela
print((df.isnull().sum()))


#apos descobrir que estão faltando alguns dados de anos na emoresa, observamos quais são os anos que estão presentes na tabela
print(df["work_year"].unique())

#filtranddo os individuos que não estão com nome na tabela
print(df[df.isnull().any(axis=1)])


# criando dataframes para uma possivel alteração de valores nulos em alguns exemplos, utilizando a biblioteca numpy == np

df_salarios = pd.DataFrame({
    'nome': ['Marcos', 'Pedro', "Ana", "Claudio", 'Val'],
    'salario':[2000, np.nan, 5000, np.nan, 100000]
})
#calculando a media e mediana desses valores e aplicando na tabela
df_salarios['media_salarial'] = df_salarios['salario'].fillna(df_salarios['salario'].mean()) #media, não é muito bom utilizar qaundo se tem valores muito grandes
df_salarios['mediana_salarial'] = df_salarios['salario'].fillna(df_salarios['salario'].median())
print(df_salarios)


#usando ffill para completar valores que não estão presentes na tabela, ex:
df_temperatura = pd.DataFrame({
    'dia_semana' : ['S', 'T', "Q", "QUI", 'SEX'],
    'temp': [30, np.nan, np.nan, 20, 19]
})

df_temperatura['preenchendo_ffill '] = df_temperatura['temp'].ffill()
#repete um valor anterior estimando que seja o mesmo
print(df_temperatura)


#utilizando bfill para preencher valores que estão faltantes só que utilizando valores decrescentes

df_temperatura = pd.DataFrame({
    'dia_semana' : ['S', 'T', "Q", "QUI", 'SEX'],
    'temp': [30, np.nan, np.nan, 20, 19]
})

df_temperatura['preenchendo_bfill'] = df_temperatura['temp'].bfill()
print(df_temperatura)

#utilizando fillna para substituir com string valores não informados

df_cidades = pd.DataFrame({
    'nome': ['Joao', 'Pedro', 'Maria', 'Lucia', 'Val'],
    'cidade':['São Paulo',np.nan, 'Curitiba', np.nan, 'Belém']
})

df_cidades['cidade_preenchida'] = df_cidades['cidade'].fillna("não informado")
print(df_cidades)


#utilizando dropna para remover valores ausentes em um dataframe...

df_limpar = df.dropna()
print(df_limpar.isnull().sum())


print(df_limpar.head())

#obtendo informações da tabela

print(df_limpar.info())

#alterando valores no dataframe

df_limpar = df_limpar.assign(work_year = df_limpar['work_year'].astype('int64'))

print(df_limpar.info())
