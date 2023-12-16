import os
import pandas as pd

def obter_clubes():
    for p, _, files in os.walk(os.path.abspath(r'C:\\Users\\Douglas\\Documents\\Scripts_Python\\Data_Brasileirao\\dados')):
        clubes = []
        for file in files:
            arquivo = pd.read_excel(os.path.join(p, file))
            for clube in arquivo['Clube']:
                clubes.append(clube)    
    return  list(dict.fromkeys(clubes))
