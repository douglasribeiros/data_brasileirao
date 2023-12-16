import requests
import pandas as pd
from bs4 import BeautifulSoup
import re

#FUNÇÃO OBTEM DOS DADOS DO CAMPEONATO BRASILEIRO DA SERIE A , DOS ANOS 2012 A 2017 DO SITE DA CFB#




def obter_dados_2012_a_2017():

    for ano in range(2012,2018):
        req = requests.get(f'https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/{ano}')
        content = req.content
        site = BeautifulSoup(content,'html.parser')
        
        tabela = site.find_all('table',attrs={'class':'table m-b-20 tabela-expandir'})
        clubes = str([i.find_all('span',attrs={'class':'hidden-xs'}) for i in tabela]).replace('<span class="hidden-xs">','').replace(' Saf','').replace(' S.a.f.','').replace('</span>','').replace('[[','').replace(']]','').replace(' ','').replace('fc','').split(',')
        pontos = str([i.find_all('th',attrs={'scope':'row'})for i in tabela]).replace('<th scope="row">','').replace('</th>','').replace('[[','').replace(']]','').split(',')
        dados = str([i.find_all('tr',attrs={'class':''}) for i in tabela]).split('<tr class="">')
        
        dados_clube = {}
        posicao = 0
        for dado in dados:
            t = re.compile(r'([-]?[0-9]?[0-9]?[0-9]){1,}</td>')    
            dados_por_clube = t.findall(str(dado))
            dados_clube.update({posicao:dados_por_clube})
            posicao = posicao + 1

        df_tabela = pd.DataFrame(columns=['Clube','PTS','J','V','E','D','GP','GC','SG','CA','CV','%'])

        i= 1
        for clube,ponto in zip(clubes,pontos):
            info = [clube,ponto]
            df_tabela.loc[i] = info+dados_clube[i]
            i = i + 1
        df_tabela.index.name = 'Posicao'
        df_tabela.to_excel(f'C:\\Users\\Douglas\\Documents\\Scripts_Python\\Data_Brasileirao\\dados\\tabela_{ano}.xlsx')    