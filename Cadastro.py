import streamlit as st
import pandas as pd
import numpy as np
import time

usu = st.text_input('Crie seu nome de usuário','Usuário')
pas = st.text_input('Crie sua senha','Senha')

butao = st.button('Criar')

if butao:
  st.write('Conta criada :D')
  usu1 = usu
  pas1 = pas
  st.write(f'Usuario {usu1} e senha {pas1}')
