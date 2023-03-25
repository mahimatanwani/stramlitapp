import streamlit as st
if st.button('First Button'):
    st.write('The first button was clicked')
    if st.button('Second Button'):
        st.write('The second button was clicked')
    