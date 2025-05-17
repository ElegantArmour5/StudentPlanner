import streamlit as st
import pandas as pd
import hashlib
import json
import os
from datetime import datetime

st.set_page_config(page_title="Student Planner", layout="centered")

USERS_FILE = "users.json"

# --- PASSWORD HASHING ---
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# --- USER DATABASE ---
def load_users():
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, "w") as f:
            json.dump({}, f)
    with open(USERS_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)

users = load_users()

# --- SESSION ---
if "username" not in st.session_state:
    st.session_state.username = None
if "mode" not in st.session_state:
    st.session_state.mode = "login"

# --- LOGIN OR REGISTER SCREEN ---
if st.session_state.username is None:
    st.title("🔐 Student Planner")
    st.write("Welcome! Please log in or register to get started.")

    mode = st.radio("Select option:", ["Log In", "Register"], horizontal=True)
    st.session_state.mode = "login" if mode == "Log In" else "register"

    username_input = st.text_input("Username")
    password_input = st.text_input("Password", type="password")

    if st.session_state.mode == "login":
        if st.button("Log In"):
            if username_input and password_input:
                if username_input in users:
                    if hash_password(password_input) == users[username_input]:
                        st.session_state.username = username_input
                        st.rerun()
                    else:
                        st.error("Incorrect password.")
                else:
                    st.error("User does not exist.")
            else:
                st.warning("Enter both username and password.")
    else:
        if st.button("Register"):
            if username_input and password_input:
                if username_input in users:
                    st.error("Username already exists.")
                else:
                    users[username_input] = hash_password(password_input)
                    save_users(users)
                    st.success("Account created! You can now log in.")
                    st.session_state.mode = "login"
                    st.rerun()
            else:
                st.warning("Please fill in all fields.")
    st.stop()

# --- USER SETUP ---
username = st.session_state.username
TASKS_FILE = f"tasks_{username}.csv"

# Load or create task DataFrame
if os.path.exists(TASKS_FILE):
    df = pd.read_csv(TASKS_FILE)
    if "Details" not in df.columns:
        df["Details"] = ""
    if "Due Date" in df.columns:
        df["Due Date"] = pd.to_datetime(df["Due Date"]).dt.date
else:
    df = pd.DataFrame(columns=["Title", "Subject", "Due Date", "Details"])

# --- SIDEBAR ---
with st.sidebar:
    st.subheader(f"👤 Logged in as: {username.capitalize()}")
    if st.button("🚪 Logout"):
        st.session_state.username = None
        st.rerun()

# --- HEADER ---
st.title(f"📘 {username.capitalize()}'s Student Planner")

# --- ADD TASK ---
st.subheader("➕ Add a New Task")
with st.form("task_form"):
    title = st.text_input("Task Title")
    subject = st.text_input("Subject")
    due_date = st.date_input("Due Date")
    details = st.text_area("Details (optional)")

    submitted = st.form_submit_button("Add Task")
    if submitted and title:
        new_task = {
            "Title": title,
            "Subject": subject,
            "Due Date": due_date,
            "Details": details
        }
        df = pd.concat([df, pd.DataFrame([new_task])], ignore_index=True)
        df.to_csv(TASKS_FILE, index=False)
        st.success(f"✅ Task '{title}' added!")
        st.rerun()

# --- TASK VIEW ---
st.subheader("📂 Your Tasks")

if df.empty:
    st.info("No tasks yet. Add some above!")
else:
    sort_by = st.radio("Sort tasks by:", ["Due Date", "Title"], horizontal=True)
    df["Due Date"] = pd.to_datetime(df["Due Date"]).dt.date
    if sort_by == "Due Date":
        df_sorted = df.sort_values("Due Date")
    else:
        df_sorted = df.sort_values("Title")

    for _, row in df_sorted.iterrows():
        with st.expander(f"📌 {row['Title']} — {row['Subject']} (Due: {row['Due Date']})"):
            st.markdown(f"**Subject:** {row['Subject']}")
            st.markdown(f"**Due Date:** {row['Due Date']}")
            st.markdown("**Details:**")
            st.write(row["Details"] or "_No additional details_")

# --- CLEAR TASKS ---
st.divider()
if st.button("🗑️ Clear All Tasks"):
    df = pd.DataFrame(columns=["Title", "Subject", "Due Date", "Details"])
    df.to_csv(TASKS_FILE, index=False)
    st.warning("All tasks cleared.")
    st.rerun()
