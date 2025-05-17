import streamlit as st
import pandas as pd
import os

# File to store tasks
TASKS_FILE = "tasks.csv"

# Load existing tasks or create empty DataFrame
if os.path.exists(TASKS_FILE):
    df = pd.read_csv(TASKS_FILE)
else:
    df = pd.DataFrame(columns=["Title", "Subject", "Due Date"])

st.title("📘 Student Planner App")

# --- Add a New Task ---
with st.form("task_form"):
    title = st.text_input("Task Title")
    subject = st.text_input("Subject")
    due_date = st.date_input("Due Date")

    submitted = st.form_submit_button("Add Task")
    if submitted and title:
        new_task = {"Title": title, "Subject": subject, "Due Date": due_date}
        df = pd.concat([df, pd.DataFrame([new_task])], ignore_index=True)
        df.to_csv(TASKS_FILE, index=False)
        st.success(f"Added task: {title}")

# --- Display Tasks ---
st.subheader("📝 Your Tasks")
if not df.empty:
    st.dataframe(df.sort_values("Due Date"))
else:
    st.info("No tasks added yet!")

# --- Optionally: Clear tasks ---
if st.button("Clear All Tasks"):
    df = pd.DataFrame(columns=["Title", "Subject", "Due Date"])
    df.to_csv(TASKS_FILE, index=False)
    st.warning("All tasks cleared.")
