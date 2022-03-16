import streamlit as st

with st.echo(code_location = "below"):
  st.write(st.secrets.username)
  st.write(st.secrets.password)
  st.write(st.secrets.fruit.applecolor)
  st.write(st.secrets.fruit.appletaste)
  st.write(st.secrets)
