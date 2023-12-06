import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(page_title="Calcular Consumo", page_icon="⚡")
st.markdown("# Calcular Consumo")
st.sidebar.header("Calcular Consumo")

st.divider()

hd = st.number_input('Digite o tempo de uso diário em horas')
nd = st.number_input('Digite o numero de dias que usou esse aparelho no mês')
opcao = st.selectbox(
    'Selecione o produto que queira calcular',
    ('Chuveiro Elétrico', 'Ar Condicionado', 'Ferro de Passar', 'Computador'))

st.divider()

if opcao == 'Chuveiro Elétrico':
    pot = 5000
    con = pot*hd*nd/1000
    with st.spinner('Carregando...'):
        time.sleep(5)
    st.write(f'Seu gasto mensal será de {con:.2f} Kw/h, portanto R$ {0.48*con:.2f}.')
if opcao == 'Ar Condicionado':
    pot = 1600
    con = pot*hd*nd/1000
    with st.spinner('Carregando...'):
        time.sleep(5)
    st.write(f'Seu gasto mensal será de {con:.2f} Kw/h, portanto R$ {0.48*con:.2f}.')
if opcao == 'Ferro de Passar':
    pot = 1500
    con = pot*hd*nd/1000
    with st.spinner('Carregando...'):
        time.sleep(5)
    st.write(f'Seu gasto mensal será de {con:.2f} Kw/h, portanto R$ {0.48*con:.2f}.')
if opcao == 'Computador':
    pot = 550
    con = pot*hd*nd/1000
    with st.spinner('Carregando...'):
        time.sleep(5)
    st.write(f'Seu gasto mensal será de {con:.2f} Kw/h, portanto R$ {0.48*con:.2f}.')
