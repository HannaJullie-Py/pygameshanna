import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Calcular Consumo", page_icon="⚡")
st.markdown("# Calcular Consumo")
st.sidebar.header("Calcular Consumo")

opcao = st.selectbox(
    'Selecione o produto que queira calcular',
    ('Chuveiro Elétrico', 'Ar Condicionado', 'Ferro de Passar', 'Computador'))

st.write('Você selecionou', opcao)
