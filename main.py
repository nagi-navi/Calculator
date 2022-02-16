import streamlit as st
import sympy as sp

from latex2sympy import process_latex

st.title('Calculator')

'''
## target formula
'''

tgt = st.text_input('')

'latex'
st.latex(tgt)

x = sp.Symbol('x')

f = process_latex.process_sympy(tgt)

'sympy'
st.write(f)
st.latex(sp.solve(f, x))