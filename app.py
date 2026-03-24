import streamlit as st
import streamlit.components.v1 as components

# إعداد الصفحة لتكون عريضة
st.set_page_config(layout="wide", page_title="مقياس تحليل البيانات")

# قراءة ملف HTML الذي أنشأناه
try:
    with open("linear_algebra_dashboard.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    
    # عرض المحتوى في Streamlit
    components.html(html_content, height=850, scrolling=True)

except FileNotFoundError:
    st.error("لم يتم العثور على ملف 'linear_algebra_dashboard.html'. تأكد من أنه موجود في نفس المجلد الذي يحتوي على ملف app.py.")