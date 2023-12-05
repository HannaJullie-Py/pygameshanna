import streamlit as st
import pandas as pd
import numpy as np
import time

st.session_state['cadastro'] = st.text_input(label="Cadastro")

def cadastro():
  st.text('Crie seu nome de usuário','Usuário')
  st.text('Crie sua senha','Senha')



butao = st.button('Criar', on_click=cadastro, args= (st.session_state['cadastro']))

if butao:
  st.write('Conta criada :D')
