import streamlit as st

st.set_page_config(page_title="журнал задач",page_icon="📋",layout="centered")
st.title("журнал задач")
st.caption("здесь будут задачи")

tasks_tab,=st.tabs(["задачи"])
with tasks_tab:
  st.write("скоро cписок задач")
  if st.button("нажми"):
    st.write("=)")
