import streamlit as st
import pandas as pd
import numpy as np


usu = st.text_input('Crie seu nome de usuário')
pas = st.text_input('Crie sua senha')
if usu and pas:
    while True:
        clear_output(True)
