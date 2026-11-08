import streamlit as st

st.title("Student Performance Analyzer")

name = st.text_input("Student Name")
marks = st.slider("Enter Marks", 0, 100, 50)

if st.button("Analyze"):
    st.write("Student:", name)
    st.write("Marks:", marks)

    if marks >= 90:
        st.success("Grade A+")
    elif marks >= 80:
        st.success("Grade A")
    elif marks >= 70:
        st.info("Grade B")
    elif marks >= 60:
        st.info("Grade C")
    elif marks >= 40:
        st.warning("Grade D")
    else:
        st.error("Fail")