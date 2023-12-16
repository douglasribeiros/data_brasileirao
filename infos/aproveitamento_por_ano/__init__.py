import os
import pandas as pd

def obter_aproveitamento_clube_ano(clube):
    for p, _, files in os.walk(os.path.abspath(r'C:\\Users\\Douglas\\Documents\\Scripts_Python\\Data_Brasileirao\\dados')):
        aproveitamento_ano = []
        for file in files:
            arquivo = pd.read_excel(os.path.join(p, file))
            filtro = arquivo.query(f'Clube=="{clube}"')
            aproveitamento = str(filtro['%'].values).replace(']','').replace('[','')
            aproveitamento_ano.append(aproveitamento)
    return aproveitamento_ano



