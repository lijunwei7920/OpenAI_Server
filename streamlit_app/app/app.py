import streamlit as st
import requests

st.title("Flask API 数据展示")

# 获取 Flask API 的数据
response = requests.get("http://flask_app:5000/api/data")
data = response.json()
#data = "hello world"
# 显示数据
st.write("从 Flask API 获取的数据：", data)
