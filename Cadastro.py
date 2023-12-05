import streamlit as st
import pandas as pd
import numpy as np
import time

usu = st.text_input('Crie seu nome de usuário','Usuário')
pas = st.text_input('Crie sua senha','Senha')

if st.button('Criar'):
                  print ('Conta criada :D')

