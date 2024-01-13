import requests
import pandas as pd
import os


# Caminho do arquivo de texto
caminho_arquivo = 'ADICIONAR ROTA DO SEU ARQUIVO.txt'

# Ler o arquivo de texto (assumindo que seja um arquivo TSV)
# Se o arquivo for CSV, você pode usar pd.read_csv() no lugar
dados = pd.read_table(caminho_arquivo, header=None)
x = 0

with open(caminho_arquivo, 'r') as arquivo:
    for linha in arquivo:
        codigos_por_linha = (linha.strip())
        # URL do site do NCBI para pesquisa
        url_ncbi = f"https://www.ncbi.nlm.nih.gov/search/api/download-sequence/?db=protein&id={codigos_por_linha}"

        # Caminho para a pasta onde você deseja salvar o arquivo
        pasta_destino = 'ADICIONE ROTA DE ONDE DESEJA SALVAR OS ARQUIVOS BAIXADOS'
        x = x + 1
        nome_arquivo = f'XXX{x}.fasta' # Nome do arquivo a ser salvo (pode ser extraído do link, se necessário)

        caminho_arquivo = os.path.join(pasta_destino, nome_arquivo) # Caminho completo do arquivo de destino

        response = requests.get(url_ncbi) # Baixar o conteúdo do arquivo

        if response.status_code == 200:
            with open(caminho_arquivo, 'wb') as f:   # Salvar o arquivo localmente
                f.write(response.content)

            print(f"Download concluído. O arquivo foi salvo em: {caminho_arquivo}")
        else:
            print(f"Falha na solicitação. Código de status: {response.status_code}")
            