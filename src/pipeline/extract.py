import os
from datetime import datetime, timedelta
import pandas as pd
import yfinance as yf

# Lista de códigos das ações da B3 (exemplo)
tickers = ['SLCE3.SA', 'SAPR4.SA', 'TUPY3.SA', 'SIMH3.SA', 'LJQQ3.SA', 'BBDC3.SA', 'BBDC4.SA', 'BBAS3.SA', 'CEAB3.SA', 'BMGB3.SA']

# Parâmetros
dias_uteis_ano = 252  # Aproximadamente 1 ano útil
hoje = datetime.today().date()

# Pasta para salvar os arquivos
output_dir = "data"
os.makedirs(output_dir, exist_ok=True)

for ticker in tickers:
    # Baixar dados do último ano útil
    data_inicio = hoje - timedelta(days=int(dias_uteis_ano * 1.5))
    df = yf.download(ticker, start=data_inicio, end=hoje + timedelta(days=1))[['Close', 'Volume']]
    df = df.dropna()
    df = df.tail(dias_uteis_ano)  # Garante 252 linhas

    # Adiciona coluna de ano e mês
    df['Ano'] = df.index.year
    df['Mes'] = df.index.month

    # Agrupa por ano e mês e salva um arquivo para cada mês
    for (ano, mes), df_mes in df.groupby(['Ano', 'Mes']):
        if not df_mes.empty:
            data_inicial = df_mes.index[0].strftime('%Y-%m-%d')
            data_final = df_mes.index[-1].strftime('%Y-%m-%d')
            filename = f"{ticker.replace('.SA','')}_{ano}_{mes:02d}_{data_inicial}_a_{data_final}.csv"
            filepath = os.path.join(output_dir, filename)
            df_mes[['Close', 'Volume']].to_csv(filepath, index_label='Date')