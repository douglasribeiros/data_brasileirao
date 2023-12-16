from pyecharts.charts import Bar
from infos.clubes import *
from infos.classificacao_por_ano import *
import streamlit.components.v1 as components
from pyecharts.charts import Bar
from pyecharts import options as opts
import streamlit as st
from PIL import Image

def pagina_desempenho():
    
    
    
    clube = st.selectbox('Escolha o Clube',obter_clubes())
    dados = obter_classificacao_clube_ano(clube)

    col1,col2 = st.columns([0.6,4])
    with col1:
        logo = Image.open(f'imagens/clubes/{clube}.png')
        st.image(logo,width=100)    
    with col2:
        c = (Bar()
            .add_xaxis(["2012",'2013','2014','2015','2016','2017','2018','2019','2020','2021','2022','2023'])
            .add_yaxis(f'', dados)
            .set_global_opts(title_opts=opts.TitleOpts(title=f'Classificação {clube} entre 2012 a 2023'),
                                toolbox_opts=opts.ToolboxOpts())
            .render_embed() # generate a local HTML file
            )
        components.html(c, width=1000, height=1000)