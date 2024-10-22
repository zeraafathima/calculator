import streamlit as st

st.title('Calculator')
st.header('This is a Calculator application')
st.subheader('Created by Fathima')
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

