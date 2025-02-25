import requests
import streamlit as st
from time import sleep
from config import API_URL

def send_post_request(product_name, product_details):
    payload = {"product_name": product_name, "product_details": product_details}
    st.write(f"Payload: {payload}")
    response = requests.post(API_URL, json=payload)

    while response.status_code != 200:
        sleep(0.1)

    response_data = response.json()
    st.write(f"Response: {response_data}")
    return response_data