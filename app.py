import numpy as np
import streamlit as st

col1, col2 = st.columns([1, 1])

with col1:
    dice = st.number_input("Roll a dice", step=1, value=6, min_value=1)
    if st.button("Roll"):
        st.write(np.random.randint(1, dice + 1))

with col2:
    number = st.number_input("Permutation size", step=1, value=1, min_value=1)
    if st.button("Permute"):
        st.write(" ".join([str(n + 1) for n in np.random.permutation(number)]))
