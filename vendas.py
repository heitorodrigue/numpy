import pandas as pd
import numpy as np
from datetime import datetime

def carregar_dados_csv(caminho_csv):
    df = pd.read_csv(caminho_csv)
    df['Data'] = pd.to_datetime(df['Data'])
    df['Quantidade Vendida'] = pd.to_numeric(df['Quantidade Vendida'])
    df['Preço Unitário'] = pd.to_numeric(df['Preço Unitário'])
    df['Valor Total'] = df['Quantidade Vendida'] * df['Preço Unitário']
    return df

def calcular_estatisticas(df):
    media_valor_total = df['Valor Total'].mean()
    mediana_valor_total = df['Valor Total'].median()
    desvio_padrao_valor_total = df['Valor Total'].std()
    produto_mais_vendido = df.groupby('Produto')['Quantidade Vendida'].sum().idxmax()
    produto_maior_valor = df.groupby('Produto')['Valor Total'].sum().idxmax()
    receita_por_regiao = df.groupby('Região')['Valor Total'].sum().to_dict()
    venda_media_dia = df.groupby('Data')['Valor Total'].sum().mean()
    return {
        "media_valor_total": media_valor_total,
        "mediana_valor_total": mediana_valor_total,
        "desvio_padrao_valor_total": desvio_padrao_valor_total,
        "produto_mais_vendido": produto_mais_vendido,
        "produto_maior_valor": produto_maior_valor,
        "receita_por_regiao": receita_por_regiao,
        "venda_media_dia": venda_media_dia
    }

def analise_temporal(df):
    df['Dia da Semana'] = df['Data'].dt.weekday
    dia_mais_vendas = df.groupby('Dia da Semana')['Valor Total'].sum().idxmax()
    variacao_diaria = df.groupby('Data')['Valor Total'].sum().diff().dropna()
    return {
        "dia_mais_vendas": dia_mais_vendas,
        "variacao_diaria": variacao_diaria
    }

caminho_csv = 'vendas.csv'
df = carregar_dados_csv(caminho_csv)
estatisticas = calcular_estatisticas(df)
temporal = analise_temporal(df)

print("Estatísticas:", estatisticas)
print("Análise Temporal:", temporal)

