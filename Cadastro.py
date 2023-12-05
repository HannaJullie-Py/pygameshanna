import streamlit as st
import pandas as pd
import numpy as np
import time

usu = st.text_input('Crie seu nome de usuário','Usuário')
pas = st.text_input('Crie sua senha','Senha')

butao = st.button('Criar', on_click=True, )

if butao:
  st.write('Conta criada :D')
  usu1 = usu
  pas1 = pas
st.write(usu1,pas1)
