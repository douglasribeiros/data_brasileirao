import os
import pandas as pd

def obter_classificacao_clube_ano(clube):
    for p, _, files in os.walk(os.path.abspath(r'C:\\Users\\Douglas\\Documents\\Scripts_Python\\Data_Brasileirao\\dados')):
        classificacao_ano = []
        for file in files:
            arquivo = pd.read_excel(os.path.join(p, file))
            filtro = arquivo.query(f'Clube=="{clube}"')
            classificacao = str(filtro['Posicao'].values).replace(']','').replace('[','')
            classificacao_ano.append(classificacao)
    return classificacao_ano



