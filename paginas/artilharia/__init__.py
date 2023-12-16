import streamlit as st

from obter_dados.artilheiros import *


def pagina_artilharia():

    ano  = st.selectbox('Escolha o ano',[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023])

    st.title(f'Artilheiros {ano}')

    st.table(obter_artilharia_ano(ano))
