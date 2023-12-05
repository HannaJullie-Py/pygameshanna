import streamlit as st
import pandas as pd
import numpy as np
import time

for seconds in range(10):
    usu = st.text_input('Crie seu nome de usuário')
    pas = st.text_input('Crie sua senha')
    time.sleep(1)
    
