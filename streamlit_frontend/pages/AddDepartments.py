import streamlit as st
import requests
from config import BASE_URL


st.header("Departmental Details")

dname = st.text_input("Department Name")
location = st.text_input("Department Location")

if st.button("Enter Details"):
    data = {"dname": dname, "loc": location}
    response = requests.post(f"{BASE_URL}department/", json=data)
    if response.status_code == 200:
        st.success("Department Details Added Successfully")
    else:
        st.error("Failed to Add")
