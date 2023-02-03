import numpy as np
import streamlit as st

number = st.number_input("Permutation size", step=1, value=1, min_value=1)
st.write(" ".join([str(n) for n in np.random.permutation(number)]))
