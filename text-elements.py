import streamlit as st
st.markdown('Streamlit is **_really_ cool**.')
st.title('This is a title')
st.header('This is a header')
st.subheader('This is a subheader')
st.caption('Display text in small font.')
code = '''def hello():
     print("Display a code block with optional syntax highlighting.")'''
st.code(code, language='python')
st.text('This is some text.')
st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')
st.latex(r'''
     a' \uparrow \nabla \text{\oe} \Reals \iff \biguplus
     ''')
