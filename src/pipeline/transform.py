import os
import glob
import pandas as pd
from typing import List


def ler_dados_pasta(data_dir: str) -> list:
    """
    Função para ler os arquivos da pasta data e retornar uma lista de dataframes.
    
    Args:
        data_dir (str): Caminho para a pasta onde os arquivos CSV estão armazenados.
        
    Returns:
        list: Lista de dataframes contendo os dados dos arquivos CSV.
    """
    # Verifica se o diretório existe
    if not os.path.exists(data_dir):
        raise FileNotFoundError(f"O diretório {data_dir} não foi encontrado.")
    
    # Lista todos os arquivos CSV na pasta
    arquivos = glob.glob(os.path.join(data_dir, "*.csv"))
    
    # Lê cada arquivo CSV e armazena em uma lista de dataframes
    dataframes = []
    for arquivo in arquivos:
        df = pd.read_csv(arquivo, index_col='Date', parse_dates=True)
        dataframes.append(df)
    
    return dataframes

"""
Função para ler os quivos da pasta data e retornornar uma lista de dataframes"""

