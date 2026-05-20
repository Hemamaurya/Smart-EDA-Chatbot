from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def get_dataset_context(df):
    return f"""Rows: {df.shape[0]}, Columns: {df.shape[1]}
Columns and types: {dict(df.dtypes.astype(str))}
Null values: {dict(df.isnull().sum())}
Sample (3 rows):
{df.head(3).to_string()}
Numeric stats:
{df.describe().round(2).to_string()}"""


def generate_code(question, df):
    context = get_dataset_context(df)
    prompt = f"""You are a Python expert. DataFrame name is 'df'.
Dataset info:
{context}

Rules:
- Return ONLY raw Python code, no markdown, no backticks, no explanation
- For charts: use matplotlib/seaborn, save with plt.savefig('output_chart.png', bbox_inches='tight'), then plt.close()
- For text/table results: convert result to JSON and print it like this:
  import json
  print("TABLE:" + json.dumps(result_dict_or_list))
- For single values: print("VALUE:" + str(result))
- Available: pandas as pd, matplotlib.pyplot as plt, seaborn as sns, numpy as np, json

Question: {question}"""

    response = groq_client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    code = response.choices[0].message.content.strip()
    if "```" in code:
        lines = [l for l in code.split("\n") if not l.strip().startswith("```")]
        code = "\n".join(lines)
    return code


def fix_code(code, error, df):
    prompt = f"""Fix this Python code error.
Code:
{code}
Error: {error}
DataFrame 'df' columns: {list(df.columns)}
Return ONLY fixed Python code, no markdown, no backticks."""

    response = groq_client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    fixed = response.choices[0].message.content.strip()
    if "```" in fixed:
        lines = [l for l in fixed.split("\n") if not l.strip().startswith("```")]
        fixed = "\n".join(lines)
    return fixed