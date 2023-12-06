import streamlit as st
import pandas as pd
import numpy as np
import time


#Título
st.set_page_config(page_title="ANAPH",page_icon="💡")
st.sidebar.header("ANAPH")
st.header('ANAPH', divider='rainbow')
st.image('https://i.imgur.com/1P4Ggm3.png',width=700)
st.write('Analisamos o seu consumo de energia elétrica!')

#Explicação
st.title('O que é?')
st.write(' **Boiola** ')
