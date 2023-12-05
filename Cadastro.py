import streamlit as st
import pandas as pd
import numpy as np
import time

usu = st.text_input('Crie seu nome de usuário','Usuário')
pas = st.text_input('Crie sua senha','Senha')

st.session_state['cadastro'] = usu and pas 

butao = st.button('Criar', on_click=True, args= (st.session_state['cadastro']))

if butao:
  st.write('Conta criada :D')
