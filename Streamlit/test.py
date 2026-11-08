# import streamlit as st

# st.title("My First Streamlit App")
# st.header("Welcome to AI Development") 
# st.write("This is my first web application.")
# st.success("Application is running successfully!")

import streamlit as st

st.title("Interactive App")

name = st.text_input("Enter your name")

age = st.number_input(
    "Enter your age",
    min_value=1,
    max_value=100
)

if st.button("Submit"):
    st.write("Hello", name)
    st.write("Your age is", age)