import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys
import json
from io import StringIO
from dotenv import load_dotenv
from llm import generate_code, fix_code

load_dotenv()

st.set_page_config(page_title="Smart EDA Chatbot", page_icon="📊", layout="wide")
st.title("📊 Smart EDA Chatbot")
st.caption("CSV upload karo aur apne data se sawaal pucho")

# Bootstrap CSS inject karo
st.markdown("""
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
""", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []
if "df" not in st.session_state:
    st.session_state.df = None
if "df_name" not in st.session_state:
    st.session_state.df_name = None
if "prefill" not in st.session_state:
    st.session_state.prefill = ""


def execute_code(code, df):
    import numpy as np
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    if os.path.exists("output_chart.png"):
        os.remove("output_chart.png")
    try:
        exec(code, {'df': df.copy(), 'pd': pd, 'plt': plt, 'sns': sns, 'np': np, 'json': json})
        error = None
    except Exception as e:
        error = str(e)
    output = sys.stdout.getvalue()
    sys.stdout = old_stdout
    chart = "output_chart.png" if os.path.exists("output_chart.png") else None
    return output, chart, error


def render_output(output):
    if not output.strip():
        return

    lines = output.strip().split("\n")
    for line in lines:
        line = line.strip()

        # TABLE format
        if line.startswith("TABLE:"):
            try:
                data = json.loads(line[6:])
                if isinstance(data, dict):
                    df_out = pd.DataFrame(list(data.items()), columns=["Category", "Value"])
                elif isinstance(data, list):
                    df_out = pd.DataFrame(data)
                else:
                    df_out = pd.DataFrame([data])

                table_html = f"""
<div style="overflow-x:auto; margin-top:10px;">
<table class="table table-bordered table-striped table-hover table-sm">
  <thead class="table-dark">
    <tr>{"".join(f"<th>{col}</th>" for col in df_out.columns)}</tr>
  </thead>
  <tbody>
    {"".join(
        "<tr>" + "".join(f"<td>{val}</td>" for val in row) + "</tr>"
        for row in df_out.values
    )}
  </tbody>
</table>
</div>"""
                st.markdown(table_html, unsafe_allow_html=True)
                st.session_state.messages.append({
                    "role": "assistant", "type": "table", "content": table_html
                })

            except Exception:
                st.write(line)

        # Single VALUE format
        elif line.startswith("VALUE:"):
            value = line[6:]
            st.markdown(f"""
<div class="alert alert-info mt-2" style="font-size:18px; font-weight:500;">
  {value}
</div>""", unsafe_allow_html=True)
            st.session_state.messages.append({
                "role": "assistant", "type": "text", "content": value
            })

        # Plain text
        else:
            st.write(line)
            st.session_state.messages.append({
                "role": "assistant", "type": "text", "content": line
            })


# SIDEBAR
with st.sidebar:
    st.header("📁 Data Upload")
    uploaded_file = st.file_uploader(
        "File upload karo (CSV, Excel, JSON, Parquet, XML)",
        type=["csv", "xlsx", "xls", "json", "parquet", "xml"]
    )

    if uploaded_file is not None:
        if st.session_state.df_name != uploaded_file.name:
            file_ext = uploaded_file.name.split(".")[-1].lower()
            if file_ext == "csv":
                st.session_state.df = pd.read_csv(uploaded_file)
            elif file_ext in ["xlsx", "xls"]:
                st.session_state.df = pd.read_excel(uploaded_file)
            elif file_ext == "json":
                st.session_state.df = pd.read_json(uploaded_file)
            elif file_ext == "parquet":
                st.session_state.df = pd.read_parquet(uploaded_file)
            elif file_ext == "xml":
                st.session_state.df = pd.read_xml(uploaded_file)
            st.session_state.df_name = uploaded_file.name

    if st.session_state.df is not None:
        st.success(f"✓ {st.session_state.df.shape[0]} rows, {st.session_state.df.shape[1]} columns")
        st.dataframe(st.session_state.df.head(5), use_container_width=True)

        st.divider()
        st.subheader("💡 Sample Questions")
        questions = [
            "Kitne null values hain?",
            "Salary ka average kya hai?",
            "Department wise employee count dikhao",
            "Pay_rate distribution chart banao output_chart.png me save karo",
            "Top 5 highest paid employees kaun hain?",
            "GenderID wise employee count dikhao"
        ]
        for q in questions:
            if st.button(q, use_container_width=True, key=q):
                st.session_state.prefill = q
                st.rerun()


# MAIN
if st.session_state.df is None:
    st.info("👈 Pehle sidebar se CSV file upload karo")
    st.stop()

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        if msg["type"] == "text":
            st.write(msg["content"])
        elif msg["type"] == "chart":
            st.image(msg["content"])
        elif msg["type"] == "table":
            st.markdown(msg["content"], unsafe_allow_html=True)

user_input = st.chat_input("Sawaal pucho...")

if st.session_state.prefill:
    user_input = st.session_state.prefill
    st.session_state.prefill = ""

if user_input:
    st.session_state.messages.append({"role": "user", "type": "text", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Soch raha hoon..."):
            try:
                code = generate_code(user_input, st.session_state.df)
                with st.expander("Generated Code"):
                    st.code(code, language="python")
                output, chart, error = execute_code(code, st.session_state.df)
                if error:
                    st.warning("Fix kar raha hoon...")
                    code = fix_code(code, error, st.session_state.df)
                    output, chart, error = execute_code(code, st.session_state.df)
                if error:
                    st.error(f"Error: {error}")
                else:
                    if output.strip():
                        render_output(output)
                    if chart:
                        st.image(chart)
                        st.session_state.messages.append({
                            "role": "assistant", "type": "chart", "content": chart
                        })
                    if not output.strip() and not chart:
                        st.info("Sawal thoda specific karo.")
            except Exception as e:
                st.error(f"Error: {str(e)}")