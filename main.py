#%%
import streamlit as st

#%%
st.title("Streamlit 入門")

st.write("Display Image")

#if st.checkbox('show Image'):       
#    img=Image.open('kao.png')
#    st.image(img,caption='kenji',use_column_width=True)

option=st.slider('君は％？',0,100,50)

'お前は',option,'％だ！'