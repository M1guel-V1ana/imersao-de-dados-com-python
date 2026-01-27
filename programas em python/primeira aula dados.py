import pandas as pd  #importando pandas como pd


df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

print(df.head()) #mostra apenas as 5 primeiras linhas

print(df.info) #informações da tabela csv


print(df.describe())

print(df.shape)


print(df.columns)

#imprimindo as linhas e colunas de maneira masi legivel


linhas, colunas = df.shape[0], df.shape[1]
print("o numero de linhas é: ", linhas)
print("o numero de colunhas é: ", colunas)

#traduzindo o nome das colunas com dicionario

traducao_colunas = {
    'work_year' : 'ano',
    'experience_level': 'senioridade', 
    'employment_type': 'emprego',
    'job_title': 'cargo',
    'salary': 'salario',
    'salary_currency': 'moeda',
    'salary_in_usd': 'usd',
    'employee_residence': 'residencia',
    'remote_ratio': 'remoto', 
    'company_location': 'empresa',
    'company_size': 'tamanho_empresa' 
}

df = df.rename(columns=traducao_colunas)

print(df.head())


print(df['senioridade'].value_counts())

print(df['emprego'].value_counts())

print(df['remoto'].value_counts())

print(df['empresa'].value_counts())

print(df['tamanho_empresa'].value_counts())

remoto_valores = {
    0: 'Presencial',
    50: 'Híbrido', 
    100: 'Remoto'
}

df['remoto'] = df['remoto'].replace(remoto_valores)

print(df['remoto'].value_counts())


tamanho_empresa_t = {
    'M': 'Média', 
    'L': 'Grande',
    'S': 'Pequeno'
}


df['tamanho_empresa'] = df['tamanho_empresa'].replace(tamanho_empresa_t)

print(df['tamanho_empresa'].value_counts())

emprego_translation = {
    'FT': 'Tempo Integral',
    'CT': 'Contrato', 
    'PT': 'Tempo Parcial',
    'FL': 'Freelancer'
}

df['emprego'] = df['emprego'].replace(emprego_translation)
print(df['emprego'].value_counts())
print(df.head(10))


print(df.describe(include= 'object'))
print(df.describe)