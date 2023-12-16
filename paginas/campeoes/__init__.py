import streamlit as st
from infos.campeoes import *
from infos.campeoes_por_ano import *

from PIL import Image


def pagina_campeoes():

    st.title('Campeões de 2012 a 2023 \n')


    campeao_por_ano = obter_campeoes_por_ano()

    for k in obter_campeoes().keys():
        quantidade = obter_campeoes()[k]
        image = Image.open(f'imagens/clubes/{k}.png')
        
        
        col1,col2,col3,col4,col5 = st.columns([2,0.1,0.1,0.1,0.1])
        taca = Image.open(f'imagens/tacas/taca.png')
            
        with col1:
            st.image(image,width=60)

        with col2:
            if quantidade >= 1:
                print(campeao_por_ano[k][0])
                st.image(taca,width=50,caption=campeao_por_ano[k][0])
            
        with col3:
            if quantidade >= 2:
                st.image(taca,width=50,caption=campeao_por_ano[k][1])
        
        with col4:
            if quantidade >= 3:
                st.image(taca,width=50,caption=campeao_por_ano[k][2])

        with col5:
            if quantidade >= 4:
                st.image(taca,width=50,caption=campeao_por_ano[k][3])



