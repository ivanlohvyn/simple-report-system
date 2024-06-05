import pandas as pd
import streamlit as st


def generate_report():
    st.title("Generate report")

    work_day = st.date_input("Date", value=pd.Timestamp.today(), key="day")
    num_tasks = st.text_input("Card ID", key="task_id")
    hours = st.text_input("Hours", key="hours")
    results = st.text_input("Results", key="results")
    work_description = st.text_area("Work Description", key="description")

    if st.button("Generate Report"):
        report_data = {
            "Date": work_day,
            "Work Description": work_description,
            "Hours": hours,
            "Number of Tasks": num_tasks,
            "Results": results,
        }
        df = pd.DataFrame([report_data])

        st.subheader("Generated Report")
        st.write(df)
        with open("reports.csv", "a") as f:
            df.to_csv(f, header=f.tell() == 0, index=False)


generate_report()
