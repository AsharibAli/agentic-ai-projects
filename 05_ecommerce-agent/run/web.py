import streamlit as st
from ui.layout import set_page_config, apply_custom_style
from ui.product_display import display_products
from data.products import products
from config import APP_TITLE
from utils.logging_config import configure_logging
import os
import sys


def main():
    """Main function to run the Streamlit application."""
    configure_logging()
    set_page_config()
    apply_custom_style()

    st.title(APP_TITLE)

    display_products(products)


def entry_point():
    """Entry point function for uv run web command."""
    # Get the directory of this script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Path to this file
    web_py_path = os.path.join(current_dir, "web.py")
    
    # Use Streamlit's CLI module to run the app
    import streamlit.web.cli as stcli
    sys.argv = ["streamlit", "run", web_py_path, "--browser.serverAddress=localhost", "--server.headless=true"]
    sys.exit(stcli.main())


if __name__ == "__main__":
    # If this script is run directly, just run the main function
    main()