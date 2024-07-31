import streamlit as st

st.title('calculator')
st.header('this is a calculator application')
st.subheader('created by fathima')
x=st.number_input(label='enter the first number')
action=st.selectbox(label='select action',options=["+","-","*","/"])
y=st.number_input(label='enter the second number')

clicked=st.button("submit")

if clicked:
    if action=="+":
        st.header(x+y)
    elif action=="-":
        st.header(x-y)
    elif action=="*":
        st.header(x*y)
    elif action=="/":
        st.header(x/y)

