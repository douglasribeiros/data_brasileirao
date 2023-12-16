import streamlit as st
import pandas as pd

def pagina_tabelas():
    ano = st.selectbox('Selecione o ano:',['2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022','2023'])    
    tabela = pd.read_excel(f'C:\\Users\\Douglas\\Documents\\Scripts_Python\\Data_Brasileirao\\dados\\tabela_{ano}.xlsx',index_col=0)
    st.table(tabela)