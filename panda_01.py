# -=-=-=-=-=-=-=-=- EXERCÍCIOS PANDAS -=-=-=-=-=-=-=-=-
# ----------------------------------
# Desafio 01: O Analista de RH (Básico)
# Objetivo: Criar um DataFrame, renomear colunas e filtrar dados.
# Tarefas:
    # 1. Crie um DataFrame com os dados;
    # 2. Renomeie a coluna 'TI' para 'Tecnologia' (dentro da coluna departamento);
    # 3. Imprima apenas os funcionários que ganham mai de R$4000
# ----------------------------------
'''nomes = 'Ana', 'Bruno', 'Carla', 'Daniel', 'Eduarda'
salario = '2500', '3200', '5800', '1500', '7000'
departamento = 'TI', 'Vendas', 'TI', 'Vendas', 'Diretoria' '''

'''import pandas as pd

dados = {
    'Nome': ['Ana', 'Bruno', 'Carla', 'Daniel', 'Eduarda'],
    'Salarios': [2500, 3200, 5800, 1500, 7000],
    'Departamentos': ['TI', 'Vendas', 'TI', 'Vendas', 'Diretoria']
}

df = pd.DataFrame(dados)

df['Departamentos'] = df['Departamentos'].replace('TI', 'Tecnologia')

funcionarios_top = df[df['Salarios'] > 4000]

print("--- DataFrame Completo (Renomeado) ---")
print(df)
print("\n--- Funcionários com Salário > 4000 ---")
print(funcionarios_top)'''

# ----------------------------------
# Desafio 02: O Inspetor de Qualidade (Limpeza)
# Objetivo: Identificar e tratar dados ausentes (NaN).
# Tarefas:
    # 1. Verifique quantos valores nulos existem em cada coluna;
    # 2. Preencha os valores nulos da coluna 'temperatura' com a média da temperatura;
    # 3. Remova qualquer linha que ainda tenha valores nulos na coluna 'pressao'.
# ----------------------------------

'''import pandas as pd
import numpy as np

dados_sensores = {
    'sensor_id': [1, 2, 3, 4, 5],
    'temperatura': [22.5, np.nan, 23.1, 21.8, np.nan],
    'pressao': [1012, 1010, np.nan, 1013, 1015]
}
df_sensor = pd.DataFrame(dados_sensores)'''

''' CONTADOR DE VALORES NULOS: '''
'''valores_nulos = df_sensor.isnull().sum()

print(valores_nulos)'''

''' PREENCHENDO VALORES NULOS '''
'''preenchendo_valores_nulos = df_sensor['temperatura'].fillna(df_sensor['temperatura'].mean())'''

''' TRATANDO A PRESSÃO '''
'''df_sensor = df_sensor.dropna(subset=['pressao'])

print(df_sensor)'''

# ----------------------------------
# Desafio 03: O Cientistas de Dados (Transformação)
# Objetivo: Criar colunas calculadas e mapear categorias.
# Imagine que você está analisando o consumo de energia:
    # 'aparelho':['Geladeira', 'Ar Condicionado', 'TV', 'Computador']
    # 'consumo_kWh':[150, 400, 30, 80]
# Tarefas:
    # 1. Crie uma nova coluna chamada 'custo_estimado', sabendo que cada 1 kWh custa R$ 0,85;
    # 2. Crie uma coluna chamada 'categoria_consumo':
        # - Se o consumo for > 100, o valor deve ser "Alto".
        # - Se for <= 100, o valor deve ser "Baixo".
    # (Dica: use df['coluna'].apply(lambda x: ...))
# ----------------------------------

'''import pandas as pd

dados_energia = {
    'aparelho':['Geladeira', 'Ar Condicionado', 'TV', 'Computador'], 
    'consumo_kWh':[150, 400, 30, 80]
}

df_energia = pd.DataFrame(dados_energia)'''

# CRIANDOA A COLUNA "custo_estimado" 
'''df_energia['custo_estimado'] = df_energia['consumo_kWh'] * 0.85

print(df_energia)'''

# CRIANDO A COLUNA "categoria_consumo"
'''df_energia['categoria_consumo'] = 'Baixo'

df_energia.loc[df_energia['consumo_kWh'] > 100, 'categoria_consumo'] = 'Alto'

print(df_energia)'''

# ----------------------------------
# Desafio 04: O Mestre das Estatísticas (Agrupamento)
# Objetivo: Usar o 'groupby' para extrair inteligência dos dados.

'''Considere esta tabela de vendas:
    - 'vendedor': ['João', 'Maria', 'João', 'Maria', 'João', 'Maria']

    - 'produto': ['A', 'A', 'B', 'C', 'C', 'B']

    - 'valor': [100, 150, 200, 50, 300, 250]'''
# Tarefas:
    # 1. Qual foi o valor total vendido por cada vendedor?
    # 2. Qual é a média de valor por produto?
# ----------------------------------

'''import pandas as pd
tabela_de_vendas = {
    'Vendedor': ['João', 'Maria', 'João', 'Maria', 'João', 'Maria'],
    'Produto': ['A', 'A', 'B', 'C', 'C', 'B'],
    'Valor': [100, 150, 200, 50, 300, 250]
}

df_venda = pd.DataFrame(tabela_de_vendas)'''

# CALCULANDO O VALOR TOTAL VENDIDO
'''vendas_vendedor = df_venda.groupby('Vendedor')['Valor'].sum()

print(vendas_vendedor)'''

# CALCULANDO A MÉDIA DE VALOR POR PRODUTO
'''media_produto = df_venda.groupby('Produto')['Valor'].mean()

print(media_produto)'''