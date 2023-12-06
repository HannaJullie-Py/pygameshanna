import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(page_title="ANAPH",page_icon="💡")
st.sidebar.header("ANAPH")

st.image('https://s4.static.brasilescola.uol.com.br/be/2021/09/usina-tres-gargantas.jpg',width=700, caption='https://brasilescola.uol.com.br/geografia/energia-hidreletrica.htm')
st.image('https://i.imgur.com/1P4Ggm3.png', width=200)
st.title('Analisamos o seu consumo de energia elétrica!')
