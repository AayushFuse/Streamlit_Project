import streamlit as st
import requests
import pandas as pd
from config import BASE_URL

st.header("Employees")

st.write(pd.DataFrame(requests.get(f"{BASE_URL}detailed_info/?skip=0&limit=100").json()).set_index('empno'))


