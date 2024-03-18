import streamlit as st
import pandas as pd
import requests
from config import BASE_URL

# Set the page to wide mode
st.set_page_config(layout="wide")


# Fetching data from the API
employee_data = requests.get(f"{BASE_URL}employees/?skip=0&limit=100").json()
department_data = requests.get(f"{BASE_URL}department/?skip=0&limit=100").json()

col1, col2 = st.columns(2)

# Displaying data in two columns
col1.write("Employee")
with col1.expander("Employee", expanded=True):
    col1.dataframe(pd.DataFrame(employee_data).set_index("empno"))

col2.write("Departments")
with col2.expander("Departments", expanded=True):
    col2.dataframe(pd.DataFrame(department_data).set_index("deptno"))
