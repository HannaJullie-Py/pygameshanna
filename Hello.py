import streamlit as st
import pandas as pd
import numpy as np

st.title('AnaPH')
st.write('#Analisamos seu consumo de energia')
df = pd.DataFrame({
  'Jogos do Pedro': ['Marvel Snap'],
  'Jogos da Hanna': ['Butterfly Soup']
})

df
