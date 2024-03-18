import streamlit as st
import requests
from config import BASE_URL


st.header("Employee Details")

ename = st.text_input("Employee Name")
job = st.text_input("Employee Job")
deptno = st.text_input("Department Number")

if st.button("Enter Details"):
    data = {"ename": ename, "job": job, "deptno": deptno}
    response = requests.post(f"{BASE_URL}employees/", json=data)
    if response.status_code == 200:
        st.success("Employee Details Added Successfully")
    else:
        st.error("Failed to Add")