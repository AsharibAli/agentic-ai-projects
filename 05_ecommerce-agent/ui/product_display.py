import streamlit as st
from services.api_service import send_post_request

def display_product(col, product_name, product_info, index):
    with col:
        st.image(product_info["image"], use_column_width=True)
        st.markdown(f"**{product_name}**")
        if st.checkbox(f"Select {product_name}", key=f"checkbox_{index}"):
            details_html = product_info["details"].replace('\n', '<br>')
            st.markdown(
                f"""
                <div style="background-color: white; padding: 10px; border-radius: 5px;">
                    <p style="white-space: pre-wrap; word-wrap: break-word; font-weight: bold; color: black;">
{details_html}
                    </p>
                </div>
                </br>
                """,
                unsafe_allow_html=True
            )
            if st.button(f"Buy {product_name}", key=f"button_{index}"):
                response = send_post_request(product_name, product_info["details"])

def display_products(products):
    all_products = list(products.items())
    for i in range(0, len(all_products), 3):
        row_products = all_products[i:i + 3]
        cols = st.columns(3)

        for j, (product_name, product_info) in enumerate(row_products):
            display_product(cols[j], product_name, product_info, i + j)

        st.write("")
        st.write("")