import streamlit as st
import pandas as pd
import numpy as np

st.title('AnaPH')
st.write('#Analisamos seu consumo de energia')
df = pd.DataFrame({
  'primeira coluna': [1, 2, 3, 4],
  'segunda coluna': [10, 20, 30, 40]
})
