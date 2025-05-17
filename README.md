# 📘 Student Planner App

An intuitive, lightweight web app to help students organize tasks, manage deadlines, and stay productive — built with **Streamlit**.

---

## ✨ Features

- ✅ Add tasks with title, subject, and due date
- 📅 View upcoming tasks in an interactive table
- 🗑️ Clear all tasks with one click
- 💾 Tasks persist locally using CSV (simple and fast)
- 🌐 Hosted on [Streamlit Cloud](https://studentplanner.streamlit.app/)

---

## 🚀 Demo

👉 Try it live: [Click here to open the app](https://studentplanner.streamlit.app/)

---

## 🛠️ Tech Stack

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)

---

## 🧪 Setup Locally

```bash
git clone https://github.com/ElegantArmour5/StudentPlanner.git
cd StudentPlanner
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
streamlit run planner_app.py
