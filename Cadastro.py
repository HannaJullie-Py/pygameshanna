import streamlit as st
import pandas as pd
import numpy as np
import time

butao = st.button('Criar')

usu = st.text_input('Crie seu nome de usuário','Usuário')
pas = st.text_input('Crie sua senha','Senha')

if butao:
  print ('Conta criada :D')
  usu and pas

