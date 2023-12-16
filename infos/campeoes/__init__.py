import pandas as pd
import os

def obter_campeoes():
    campeoes = []
    clubes_campeoes = {}
    for p, _, files in os.walk(os.path.abspath(r'dados/')):
        for file in files:
            arquivo = pd.read_excel(os.path.join(p, file))          
            campeoes.append(str(arquivo['Clube'][0]))
    clubes = list(dict.fromkeys(campeoes))

    for clube in clubes:
        quantidade = campeoes.count(clube)
        clubes_campeoes.update({clube:quantidade})
    
    return clubes_campeoes




