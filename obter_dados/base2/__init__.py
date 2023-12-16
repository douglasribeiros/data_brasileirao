import requests
import pandas as pd
from bs4 import BeautifulSoup
import re

#FUNÇÃO OBTEM DOS DADOS DO CAMPEONATO BRASILEIRO DA SERIE A , DOS ANOS 2018 A 2023 DO SITE DA CFB#


def obter_dados_2018_a_2023():

    for ano in range(2018,2024):
        req = requests.get(f'https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/{ano}')
        content = req.content
        site = BeautifulSoup(content,'html.parser')
        
        tabela = site.find_all('tr',attrs={'class':'expand-trigger'})
        clubes = [i.find('span',attrs={'class':'hidden-xs'}).text for i in tabela]
        pontos = [i.find('th',attrs={'scope':'row'}).text for i in tabela]
        dados = [i.find_all('td') for i in tabela]

        i=1

        df_tabela = pd.DataFrame(columns=['Clube','PTS','J','V','E','D','GP','GC','SG','CA','CV','%'])


        for dado,clube,ponto in zip(dados,clubes,pontos):
            dado_clubes = str(dado).split('\n</td>,')
            t = re.compile(r'([-]?[0-9]?[0-9]?[0-9]){1,}</td>')
            dados_clubes = t.findall(str(dado_clubes))
            clube = str(clube).replace(' Saf','').replace(' S.a.f.','').replace(' ','').replace('fc','').replace('Mineiro','')
            info = [clube,ponto]
            info_final = info+dados_clubes
            df_tabela.loc[i] = info_final
            i = i + 1
        df_tabela.index.name = 'Posicao'
        df_tabela.to_excel(f'C:\\Users\\Douglas\\Documents\\Scripts_Python\\Data_Brasileirao\\dados\\tabela_{ano}.xlsx')    