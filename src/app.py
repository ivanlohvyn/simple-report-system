import streamlit as st

from pages.reports import generate_report
from pages.vizualize import visualize_data


def main():
    st.sidebar.title("Navigation")
    page_options = ["Generate Report", "Visualize Data"]
    page_selection = st.sidebar.radio("Go to", page_options)

    if page_selection == "Generate Report":
        generate_report()
    elif page_selection == "Visualize Data":
        visualize_data()


if __name__ == "__main__":
    main()
