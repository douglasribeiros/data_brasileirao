import os
import pandas as pd

def obter_pontos_clube_ano(clube):
    for p, _, files in os.walk(os.path.abspath(r'C:\\Users\\Douglas\\Documents\\Scripts_Python\\Data_Brasileirao\\dados')):
        pontos_ano = []
        for file in files:
            arquivo = pd.read_excel(os.path.join(p, file))
            filtro = arquivo.query(f'Clube=="{clube}"')
            ponto = str(filtro['PTS'].values).replace(']','').replace('[','')
            pontos_ano.append(ponto)
    return pontos_ano



