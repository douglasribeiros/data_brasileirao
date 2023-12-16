import pandas as pd
import os


def obter_campeoes_por_ano():
    campeoes = []
    clubes = []
    campeoes_por_ano = {}
    for p, _, files in os.walk(os.path.abspath(r'dados/')):
        for file in files:
            arquivo = pd.read_excel(os.path.join(p, file))     
            clube = str(arquivo['Clube'][0])
            ano = str(file).replace('.xlsx','').replace('tabela_','')
            clubes.append(clube)
            campeoes.append(f'{clube}:{ano}')
    clubes = list(dict.fromkeys(clubes))

    for clube in clubes:
        ano = []
        for campeao in campeoes:
            if str(clube) in str(campeao):
                ano.append(str(campeao).split(':')[-1])    
        campeoes_por_ano.update({clube:ano})
    return campeoes_por_ano

