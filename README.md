# 📊 Smart EDA Chatbot
# An AI-powered Exploratory Data Analysis chatbot built with Python, Groq API (LLaMA 3.3), and Streamlit.

# 🚀 Features
- Upload CSV, Excel, JSON, Parquet, XML files
- Ask questions in natural language
- Auto-generates Python code using LLM
- Shows results in Bootstrap tables and charts
- Auto error fixing if generated code fails

# 🛠️ Tech Stack
- Python, Pandas, NumPy
- Matplotlib, Seaborn
- Groq API (LLaMA 3.3 70B)
- Streamlit
- Bootstrap 5

# ⚙️ Setup
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Add Groq API key in `.env` file: `GROQ_API_KEY=your_key`
4. Run: `streamlit run app.py`

# 📊 Data Overview Questions

Q1-Kitne rows aur columns hain?
Q2-Dataset ki summary statistics dikhao

# 🔍 Missing Values

Q1-Har column mein kitne null values hain?
Q2-Null values ka percentage dikhao

## 📈 Charts & Visualization

Q1-Salary ka histogram chart banao output_chart.png me save karo

Q2-State wise employee count bar chart banao output_chart.png me save karo

Q3-Absences ka boxplot banao output_chart.png me save karo

# 💰 Salary Analysis

Sabse zyada salary kitni hai?
Top 10 highest paid employees kaun hain?
Salary ka median kya hai?

# 👥 Employee Analysis

Department wise employee count dikhao
EmploymentStatus wise employee count dikhao

# ⭐ Performance Analysis

PerformanceScore wise employee count dikhao
Sabse zyada PerformanceScore wale top 5 employees kaun hain?

# 📅 Date & Tenure Analysis

Kitne employees terminated hain?
TermReason wise count dikhao

# 🔗 Correlation Analysis

Salary aur PerformanceScore ka scatter plot banao output_chart.png me save karo
Sabhi numeric columns ka correlation heatmap banao output_chart.png me save karo

# 🎯 Advanced Questions

Sabse zyada absenteeism kis department mein hai?
Remote wale employees kitne hain?




