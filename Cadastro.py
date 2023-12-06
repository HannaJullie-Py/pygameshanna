import streamlit as st
import pandas as pd
import numpy as np
import time

st.image('https://s4.static.brasilescola.uol.com.br/be/2021/09/usina-tres-gargantas.jpg',width=700, caption='https://brasilescola.uol.com.br/geografia/energia-hidreletrica.htm')
st.title('ANAPH - Analisamos o seu consumo de energia elétrica!')

usu = st.text_input('Crie seu nome de usuário','Usuário')
pas = st.text_input('Crie sua senha','Senha')

butao = st.button('Enter em cada uma das caixas para criar')

if butao:
  st.write('Conta criada :D')

