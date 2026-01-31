#importando bibliotecas para o dashboard
import  pandas as pd
import plotly.express as px
import streamlit as st # usado para criar e costumizar o compartilhamento de web apps

#__config da pagina
#definindo o titulo da página, layout e largura

st.set_page_config(
    page_title= "Dashboard de Sálarios na Área de Dsdos",
    page_icon="📊",
    layout = 'wide',
)


#carregamento dos dados da planilha em csv

df = pd.read_csv("https://raw.githubusercontent.com/vqrca/dashboard_salarios_dados/refs/heads/main/dados-imersao-final.csv")

#barra lateral(filtros)
st.sidebar.header("🕵🏻 Filtros") #cabeçalho da barra de pesquisa

#filtrando por ano
anos_disponiveis = sorted(df['ano'].unique()) #organizado em valores únicos
anos_selecionados = st.sidebar.multiselect("Anos", anos_disponiveis, default= anos_disponiveis) #opção de cada um dos anos

#filtrando por Senioridade
senioridades_disponiveis = sorted(df['senioridade'].unique())
senioridades_selecionadas = st.sidebar.multiselect('Senioridade', senioridades_disponiveis, default= senioridades_disponiveis)

#filtrando por tipo de contrato
contratos_disponiveis = sorted(df['contrato'].unique())
contratos_selecionados = st.sidebar.multiselect("Contratos", contratos_disponiveis, default = contratos_disponiveis)

#filtrando por tamanho da empresa
tamanhos_disponiveis = sorted(df['tamanho_empresa'].unique())
tamanhos_selecionados = st.sidebar.multiselect("Tamanho da Empresa", tamanhos_disponiveis, default = tamanhos_disponiveis)


#implemetando uma filtragem por dataframes
#___ Filtragem dos DataFrames___
# o dataframe é filtrado com base nas seleções feitas na barra lateral
df_filtrador = df[
    (df['ano'].isin(anos_selecionados))&
    (df['senioridade'].isin(senioridades_selecionadas))&
    (df['contrato'].isin(contratos_selecionados))&
    (df['tamanho_empresa'].isin(tamanhos_selecionados))
]

#Conteúdo principal da página

st.title("🔎📊 Dashboard de Ánalise de Salário na Área de Dados")
st.markdown("Explore os dados salariais na área de dados nos últimos anos. Ultilize os filtros à esquerda.")

# métricas principais (KPIS)

st.subheader("Métricas gerais (Salário anual em USD)")

# utilizando o if else, para casa der algum valor errdado no df ele devolve as variaveis vazias
if not df_filtrador.empty:
    salario_medio = df_filtrador['usd'].mean()
    salario_maximo = df_filtrador['usd'].max()
    total_registros = df_filtrador.shape[0]
    cargo_frequente = df_filtrador['cargo'].mode()[0]
else:
    salario_medio, salario_mediano, salario_maximo, total_registros, cargo_frequente = 0, 0, 0, ""

#dividindo as metricas em colunas
col1, col2, col3, col4 = st.columns(4)
col1.metric("Salário médio", f"{salario_medio:,.0f}")
col2.metric("Salário máximo", f"{salario_maximo:,.0f}")
col3.metric("Total registros", f"{total_registros:,}")
col4.metric("Cargo Frequente", cargo_frequente)

st.markdown("---")




#utilizando gráficos para exibir informações

st.subheader("Gráficos 📈")

col_graf1, colf_graf2 = st.columns(2)
#10 cargos por salario medio
with col_graf1:
    if not df_filtrador.empty:
        top_cargos = df_filtrador.groupby('cargo')['usd'].mean().nlargest(10).sort_values(ascending=True).reset_index() #agrupamento
        grafico_cargos = px.bar(
            top_cargos,
            x='usd',
            y='cargo',
            orientation='h',
            title = 'Top 10 cargos por salario médio',
            labels = {'usd': 'Média salarial anual (USD)', 'cargo': ''}
        )
        grafico_cargos.update_layout(title_x=0.1, yaxis={'categoryorder': 'total ascending'}) #mover o titulo
        st.plotly_chart(grafico_cargos, use_container_width=True) #exibir o gráfico
    else:
        st.warning("Nenhum dado para exibir no gráfico de cargos")


# Distribuição anual dos salários - histograma
with colf_graf2:
    if not df_filtrador.empty:
        grafico_hist = px.histogram(
            df_filtrador,
            x = 'usd',
            nbins= 30,
            title = "Distribuição de salários anuais",
            labels= {'usd': 'Faixa salarial (USD)', 'count': ''}
        )
        grafico_hist.update_layout(title_x = 0.1)
        st.plotly_chart(grafico_hist, use_container_width=True)
    else:
        st.warning('Nenhum dado para exibir no gráfico de distribuição.')



col_graf3, col_graf4 = st.columns(2)

with col_graf3:
    if not df_filtrador.empty:
        remoto_contagem = df_filtrador['remoto'].value_counts().reset_index()
        remoto_contagem.columns = ['tipo_trabalho', 'quantidade']
        grafico_remoto = px.pie(
            remoto_contagem,
            names='tipo_trabalho',
            values='quantidade',
            title='Proporção dos tipos de trabalho',
            hole=0.5
        )
        grafico_remoto.update_traces(textinfo='percent+label')
        grafico_remoto.update_layout(title_x=0.1)
        st.plotly_chart(grafico_remoto, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico dos tipos de trabalho.")



with col_graf4:
    if not df_filtrador.empty:
        df_ds = df_filtrador[df_filtrador['cargo'] == 'Data Scientist']
        media_ds_pais = df_ds.groupby('residencia_iso3')['usd'].mean().reset_index()
        grafico_paises = px.choropleth(media_ds_pais,
            locations='residencia_iso3',
            color='usd',
            color_continuous_scale='rdylgn',
            title='Salário médio de Cientista de Dados por país',
            labels={'usd': 'Salário médio (USD)', 'residencia_iso3': 'País'})
        grafico_paises.update_layout(title_x=0.1)
        st.plotly_chart(grafico_paises, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico de países.")

#criando a tabela de dados detalhada

st.subheader("Dados com Detalhes")
st.dataframe(df_filtrador)