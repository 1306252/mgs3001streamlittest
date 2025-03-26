import streamlit as st
st.title("My first webapp")

annual_salary = st.number_input("Enter your annual salary:")
year_work = st.number_input("Enter your Year of work:")
if st.button("Submit"):
    if annual_salary >= 500000 and year_work >= 5:
        st.write("Your applicxation is accpeted")
else:
        st.write("Sory your applicxation is not accpeted")

