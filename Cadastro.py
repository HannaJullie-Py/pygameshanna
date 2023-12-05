import streamlit as st
import pandas as pd
import numpy as np
import time

def cadastro():
  usu = st.text_input('Crie seu nome de usuário','Usuário')
  pas = st.text_input('Crie sua senha','Senha')

st.session_state['cadastro'] = cadastro

butao = st.button('Criar', on_click=cadastro, args= (st.session_state['cadastro']))

if butao:
  st.write('Conta criada :D')

