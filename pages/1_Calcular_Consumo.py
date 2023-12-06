import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(page_title="Calcular Consumo", page_icon="⚡")
st.markdown("# Calcular Consumo")
st.sidebar.header("Calcular Consumo")



hd = st.number_input('Digite o tempo de uso diário em horas')
nd = st.number_input('Digite o numero de dias que usou esse aparelho no mês')

opcao = st.selectbox(
    'Selecione o produto que queira calcular',
    ('Chuveiro Elétrico', 'Ar Condicionado', 'Ferro de Passar', 'Computador'))
if opcao == 'Chuveiro Elétrico':
    pot = 5000
    con = pot*hd*nd/1000
    with st.spinner('Carregando...'):
        time.sleep(5)
    st.write(f'Seu gasto mensal será de {con} Kw/h, portanto R$ {0.48*con:.2f}.')
