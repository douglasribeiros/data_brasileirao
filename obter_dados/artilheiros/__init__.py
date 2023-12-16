import requests
import pandas as pd
from bs4 import BeautifulSoup
import re


def obter_artilharia_ano(ano):

   
    req = requests.get(f'https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/{ano}')
    content = req.content
    site = BeautifulSoup(content,'html.parser')
    tabela_artilharia = site.find_all('table',attrs={'class':'table border-body'})
    tabela_gols = site.find_all('th',attrs={'class':'text-center','scope':'row'})
    jogadores = str([i.find_all('a') for i in tabela_artilharia]).split('</a>')
    
    artilharia = {}
    posicao = 0
    for i in range(0,30,2):
        
        nome = jogadores[i].split('target="_blank">')[-1]   
        apelido = jogadores[i+1].split('target="_blank">')[-1] 
        artilharia.update({posicao:[nome,apelido]})
        posicao = posicao + 1
    
    for k in artilharia.keys():
        gol  = str(tabela_gols[k]).replace('<th class="text-center" scope="row">','').replace('</th>','')
        artilharia[k].append(gol)

    df_artilharia = pd.DataFrame.from_dict(artilharia, orient ='index',columns=['Nome','Apelido','Gols'])

    return df_artilharia



