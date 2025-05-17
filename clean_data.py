import pandas as pd

# Nome do arquivo CSV
nome_do_arquivo = 'dadoscru.csv'

# Ignorar colunas 
colunas_a_ignorar = ['Cod.', 'ald']

try:
    df = pd.read_csv(nome_do_arquivo)
except FileNotFoundError:
    print(f"Erro: O arquivo '{nome_do_arquivo}' não foi encontrado.")
    exit()
except Exception as e:
    print(f"Ocorreu um erro ao ler o arquivo: {e}")
    exit()

# Remover Colunas a Ignorar
df_filtrado = df.drop(columns=colunas_a_ignorar, errors='ignore')
print("\nDataFrame após remover colunas:", colunas_a_ignorar)
print(df_filtrado)

# Remover Linhas com Valores Ausentes
df_limpo = df_filtrado.dropna()  # Remove linhas com *qualquer* NaN
print("\nDataFrame após remover linhas com NaNs:")
print(df_limpo)

# Análise de Valores Ausentes (Após Limpeza)
print("\n--- Análise de Valores Ausentes (Após Limpeza) ---")

# Identifica os valores ausentes (no DataFrame limpo)
valores_ausentes = df_limpo.isna()

# Conta os valores ausentes por coluna
contagem_ausentes_por_coluna = valores_ausentes.sum()
print("\nContagem de valores ausentes por coluna:\n", contagem_ausentes_por_coluna)

# Filtra as linhas com valores ausentes
linhas_com_ausentes = df_limpo[df_limpo.isna().any(axis=1)]
print("\nLinhas com valores ausentes:\n", linhas_com_ausentes)

# Identifica as colunas com valores ausentes
colunas_com_ausentes = df_limpo.columns[df_limpo.isna().any()].tolist()
print("\nColunas com valores ausentes:", colunas_com_ausentes)

# Salvar o DataFrame Tratado em CSV
nome_arquivo_tratado = 'tratados.csv'
df_limpo.to_csv(nome_arquivo_tratado, index=False)  # index=False evita salvar o índice
print(f"\nDataFrame tratado salvo como '{nome_arquivo_tratado}'")