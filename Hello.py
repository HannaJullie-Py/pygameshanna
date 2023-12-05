import streamlit as st
import pandas as pd
import numpy as np
import time

apagar = st.empty()

with apagar.container():
    usu = st.text_input('Crie seu nome de usuário')
    pas = st.text_input('Crie sua senha')
apagar.empty()    
