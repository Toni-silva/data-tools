# Tratamento de Dados Ausentes em CSV com Python

Este repositório contém um script Python (`clean_data.py`) que utiliza a biblioteca Pandas para tratar dados ausentes em arquivos CSV. O script oferece funcionalidades para limpar e preparar os dados, incluindo a remoção de colunas e linhas com valores faltantes, e salva o resultado em um novo arquivo CSV.

## Funcionalidades

O script realiza as seguintes operações:

1.  **Leitura do Arquivo CSV:**
    * Lê um arquivo CSV especificado usando `pandas.read_csv()`.
    * Trata exceções para arquivos não encontrados ou erros de leitura.

2.  **Remoção de Colunas (Opcional):**
    * Permite especificar uma lista de colunas a serem excluídas do DataFrame.
    * Utiliza `pandas.DataFrame.drop()` para remover as colunas.

3.  **Remoção de Linhas com Valores Ausentes:**
    * Remove as linhas que contêm pelo menos um valor ausente (`NaN`).
    * Utiliza `pandas.DataFrame.dropna()` para realizar a remoção.

4.  **Análise de Valores Ausentes:**
    * Identifica e conta os valores ausentes no DataFrame resultante.
    * Exibe a contagem de valores ausentes por coluna.
    * Exibe as linhas que ainda contêm valores ausentes (se houver).
    * Lista as colunas que possuem valores ausentes (se houver).

5.  **Salvamento do Arquivo Tratado:**
    * Salva o DataFrame limpo em um novo arquivo CSV chamado `tratados.csv`.
    * Utiliza `pandas.DataFrame.to_csv()` para salvar o arquivo.

## Pré-requisitos

* **Python 3.x**
* **Pandas** (instalado via `pip install pandas`)

## Como Usar

1.  **Preparação:**
    * Coloque o arquivo CSV que você deseja tratar no mesmo diretório do script ou forneça o caminho completo para o arquivo.
    * Se você deseja remover colunas específicas, modifique a lista `colunas_a_ignorar` no script com os nomes das colunas que deseja excluir.

2.  **Execução:**
    * Execute o script Python a partir do terminal:

        ```bash
        python clean_data.py
        ```

3.  **Saída:**
    * O script exibirá informações sobre o processo de tratamento de dados no terminal.
    * Um novo arquivo CSV chamado `tratados.csv` será criado no mesmo diretório, contendo os dados limpos.

## Arquivos

* `clean_data.py`: O script Python principal para tratamento de dados ausentes.
* `README.md`: Este arquivo, fornecendo documentação sobre o script.
* `dadoscru.csv` (Exemplo): Um arquivo CSV de exemplo (opcional, você deve usar seu próprio arquivo).

## Observações

* Certifique-se de ajustar a variável `nome_do_arquivo` no script para o nome do seu arquivo CSV de entrada.
* A lista `colunas_a_ignorar` permite que você personalize quais colunas são removidas antes da análise de valores ausentes. Adapte-a conforme necessário.
* O script remove todas as linhas que contêm *qualquer* valor ausente após a remoção das colunas especificadas.
* O arquivo de saída `tratados.csv` é salvo no mesmo diretório do script.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests para melhorar o script.
