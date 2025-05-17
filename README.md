# 📘 Student Planner App

A secure, smart, and user-specific task planner designed for students to organize assignments, manage deadlines, and boost productivity — all through a clean and interactive **Streamlit** interface.

---

## ✨ Features

- 🔐 **User Registration & Login** — accounts secured with SHA-256 hashed passwords
- 🧑‍💻 **User-Specific Task Lists** — each student sees only their tasks
- ✅ **Add Tasks** with title, subject, due date, and optional notes
- 📂 **Sort Tasks** by title or deadline
- 📄 **Expandable Task View** — click to reveal task details
- 🗑️ **Clear All Tasks** with one click
- 🔄 **Auto Refresh** after adding or clearing tasks
- 💾 **Persistent Storage** using CSV files (`tasks_<username>.csv`)
- 🌐 **Hosted on Streamlit Cloud** for easy access anywhere

---

## 🚀 Demo

👉 Try it live: [Click here to open the app](https://studentplanner.streamlit.app/)

---

## 🛠️ Tech Stack

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Hashlib](https://docs.python.org/3/library/hashlib.html) for password hashing
- [JSON](https://www.json.org/) for user database

---

## 🧪 Run Locally

```bash
# Clone the repo
git clone https://github.com/ElegantArmour5/StudentPlanner.git
cd StudentPlanner

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run planner_app.py
