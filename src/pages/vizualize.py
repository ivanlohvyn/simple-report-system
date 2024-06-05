import pandas as pd
import streamlit as st


def visualize_data():
    st.title("Day Reports")

    df = pd.read_csv("reports.csv")
    st.write(df)
    df["Date"] = pd.to_datetime(df["Date"])

    monthly_results = df.groupby(df["Date"].dt.month)["Results"].sum()

    st.subheader("Total Number of Monthly Results")
    st.write(monthly_results)


visualize_data()
