import streamlit as st

st.title("Titanica")

st.markdown(
    "<img src='https://subpng.com/images/hd/titanic-ship-png-14-8ugan97epbykmc0k.jpg' width='300' style='display: block; margin: 0 auto;'>", unsafe_allow_html=True
)
st.markdown("<br/>", unsafe_allow_html=True)

st.markdown("""
    This project aims to demonstrate the data analysis of the popular Titanic dataset using Python's data science libraries including:\n\n

    -  pandas
    - matplotlib
    - numpy
    - sklearn\n\n
    
    This project will help to predict the survival of the passenger based on given input like PClass, Sex, Fare and other features which will be considered followed by returning the survival class as output.
""")

