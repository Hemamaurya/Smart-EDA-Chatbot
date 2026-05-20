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

# 📊 Data Overview
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Q1 → Dataset mein total kitne rows, columns aur missing values hain — ek saath batao
Q2 → Har column ka data type aur null percentage ek table mein dikhao

# 📈 Charts & Visualization
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Q3 → Department wise employee count ka attractive bar chart banao output_chart.png me save karo
Q4 → Salary distribution ka histogram with KDE curve banao output_chart.png me save karo

# 💰 Salary Analysis
━━━━━━━━━━━━━━━━━━━━━━━
Q5 → Department wise average, minimum aur maximum salary ek table mein dikhao
Q6 → Top 10 highest paid employees ke naam aur salary dikhao

# 👥 Employee Analysis
━━━━━━━━━━━━━━━━━━━━━━━━
Q7 → GenderID aur MaritalDesc wise employee count ek saath dikhao
Q8 → RecruitmentSource wise employee count dikhao — sabse popular source kaun sa hai

# ⭐ Performance Analysis
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Q9 → Department wise average PerformanceScore aur EngagementSurvey dikhao
Q10 → Top 5 highest PerformanceScore wale employees ke naam aur department dikhao

# 🔗Correlation Analysis
━━━━━━━━━━━━━━━━━━━━━━━━━━
Q11 → Salary aur Absences ka scatter plot banao output_chart.png me save karo
Q12 → Sabhi numeric columns ka correlation heatmap banao output_chart.png me save karo

# 🎯 Advanced Insights
━━━━━━━━━━━━━━━━━━━━━━━━━
Q13 → Sabse zyada absenteeism kis department mein hai — bar chart banao output_chart.png me save karo
Q14 → EmploymentStatus wise employee count aur unki average salary ek table mein dikhao
Q13 → Sabse zyada absenteeism kis department mein hai — bar chart banao output_chart.png me save karo

Q14 → EmploymentStatus wise employee count aur unki average salary ek table mein dikhao
