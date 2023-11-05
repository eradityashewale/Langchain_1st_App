import os
from apikey import apikey

import streamlit as st
from langchain.llms import OpenAI

os.environ['OPENAI_API_KEY'] = apikey

st.title('Medium Article Generator')
topic = st.text_input('Enter your topic')

llm = OpenAI(temperature=0.9)

if topic:
    response = llm(topic)
    st.write(response)
