# 📊 Smart EDA Chatbot

An AI-powered Exploratory Data Analysis chatbot built with Python, Groq API (LLaMA 3.3), and Streamlit.

## 🚀 Features
- Upload CSV, Excel, JSON, Parquet, XML files
- Ask questions in natural language
- Auto-generates Python code using LLM
- Shows results in Bootstrap tables and charts
- Auto error fixing if generated code fails

## 🛠️ Tech Stack
- Python, Pandas, NumPy
- Matplotlib, Seaborn
- Groq API (LLaMA 3.3 70B)
- Streamlit
- Bootstrap 5

## ⚙️ Setup
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Add Groq API key in `.env` file: `GROQ_API_KEY=your_key`
4. Run: `streamlit run app.py`

## 📸 Demo
Ask questions like:
- "Department wise employee count dikhao"
- "Top 5 highest paid employees kaun hain?"
- "Salary distribution chart banao"
