import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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


#usando ffill para completar valores que não estão presentes na tabela ex:
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



# Vamos criar gráficos...
print(df_limpar.head())
# primeiramente obsevamos os valores do nosso novo DataFrame com os campos não preenchidos apagados

#usar pandas para construção de um gráfico, no caso matplotlib
#df_limpar['experience_level'].value_counts().plot(kind = 'bar', title = 'Distribuicao_experiencia')
#plt.show()

# calculando o salário médio para cada um dos niveis

#sns.barplot(data = df_limpar, x='experience_level', y='salary_in_usd')
#plt.show()


# construção de um gráfico com tamanhos padroes usando o plt
plt.figure(figsize=(10,5))
sns.barplot(data = df_limpar, x='experience_level', y='salary_in_usd')
#criando um titulo pro gráfico
plt.title("Salario médio por nivel de experiencia")
#titulo do eixo "x"
plt.xlabel("nivel de experiencia")
#titulo do eixo "y"
plt.ylabel("salario medio anual em dolar")
# exibindo o gráfico
plt.show()


#calculando a estistica para uma melhor representação dos gráficos
df_limpar.groupby('experience_level')['salary_in_usd'].mean().sort_values(ascending=False)

#utilizando uma variavel para armazenar os valores
order = df_limpar.groupby('experience_level')['salary_in_usd'].mean().sort_values(ascending=False).index
print(order)


# cosntruindo mais um gráfico só que de maneira ordenada
plt.figure(figsize = (10,5))
sns.barplot(data = df_limpar, x='experience_level', y='salary_in_usd', order = order)
plt.title("salario medio organizado")
plt.xlabel("nivel de experiencia")
plt.ylabel("salario medio anual em dolar")
plt.show()

#utilizando o bin para largura do gráfico
plt.figure(figsize=(10,5))
sns.histplot(df_limpar['salary_in_usd'], bins = 50, kde = True)
plt.title("Distribuição dos salarios anuais")
plt.xlabel("Nivel de experiencia")
plt.ylabel("salario medio anual")
plt.show()


#criando gráfico com quartis

plt.figure(figsize=(10,5))
sns.boxplot(x = df_limpar['salary_in_usd'])
plt.title("Distribuição anual do salario")
plt.xlabel("salario in usd ")
plt.show()

#distribuição dos quartis por nivel de experiencia:

plt.figure(figsize=(10,5))
sns.boxplot(x = 'experience_level', y = 'salary_in_usd', data = df_limpar, order = order)
plt.title("Distribuição por senioridade")
plt.xlabel('nivel de experiencia')
plt.ylabel('salario em usd')
plt.show()


plt.figure(figsize=(10,5))
sns.boxplot(x = 'experience_level', y = 'salary_in_usd', data= df_limpar, order = order, palette= 'Set2', hue = 'experience_level') # Usando a variável 'order' já definida
plt.title('Distribuição por senioridade')
plt.xlabel('nivel de experiencia')
plt.ylabel('salario em usd')
plt.show()

#impot da biblioteca para criar gráficos interativos
import plotly.express as px
avg_salary_by_experience = df_limpar.groupby('experience_level')['salary_in_usd'].mean().sort_values(ascending=False).reset_index()

fig = px.bar(
    avg_salary_by_experience,
    x='experience_level',
    y='salary_in_usd',
    title='Média Salarial por Nível de Experiência (Plotly)',
    labels={'experience_level': 'Nível de Experiência', 'salary_in_usd': 'Salário Médio Anual (USD)'},
    color='experience_level', # Colorir as barras por nível de experiência
    category_orders={'experience_level': order} # Usar a ordem definida anteriormente
)

fig.show()

#utilizando a mesma biblioteca para criar um gráfico de pizza/torta

remote_contagem = df_limpar['remote_ratio'].value_counts().reset_index()
remote_contagem.columns =['tipo_trabalho', 'quantidade']
fig = px.pie(
    remote_contagem,
    names = 'tipo_trabalho',
    values = 'quantidade',
    title='Proporção dos Tipos de Trabalho Remoto',
    hole= 0.5,
    color='tipo_trabalho' # Corrigido para uma coluna existente no DataFrame remote_contagem
    # category_orders={'experience_level': order} foi removido pois não é aplicável aqui
)

fig.show()




remote_contagem = df_limpar['remote_ratio'].value_counts().reset_index()
remote_contagem.columns =['tipo_trabalho', 'quantidade']
fig = px.pie(
    remote_contagem,
    names = 'tipo_trabalho',
    values = 'quantidade',
    title='Proporção dos Tipos de Trabalho Remoto',
    hole= 0.5,
    color='tipo_trabalho' # Corrigido para uma coluna existente no DataFrame remote_contagem
    # category_orders={'experience_level': order} foi removido pois não é aplicável aqui
)

fig.update_traces(textinfo='percent+label')
fig.show()