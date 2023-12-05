import streamlit as st
import pandas as pd
import numpy as np
import time

log = ['usuario','senha']

for seconds in range(220):
    usu = st.text_input('Crie seu nome de usuário')
    pas = st.text_input('Crie sua senha')
    
    
