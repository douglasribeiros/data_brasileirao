from obter_dados import *
from paginas import *
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

with st.sidebar:
    image = Image.open('imagens/logo.png')
    st.image(image,width=140)
    st.title('Data Brasileirão')
    selected = option_menu("", ["Tabelas","Desempenho Clubes","Campeões","Atualizar Dados","Artilharia"], menu_icon="cast", default_index=1)
    st.caption('Dados disponibilizados pela CBF de 2012 a 2023')

if selected == "Campeões":
    pagina_campeoes()                           
elif selected == 'Tabelas':
    pagina_tabelas()    
elif selected == 'Desempenho Clubes':
    pagina_desempenho() 
elif selected == 'Atualizar Dados':
    obter_dados()       
elif selected == 'Artilharia':
    pagina_artilharia()    