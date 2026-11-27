import streamlit as st
import json 
from pathlib import Path
from uuid import uuid4

data_file=Path.home() / ".task_journal" / "tasks.json"
categories=["Личное","Домашнее","Дз по репетиторам"]

def load_tasks():
  try:
    return json.loads(data_file.read_text(encoding="utf-8"))
  except FileNotFoundError:
    return []

def save_tasks(tasks):
  data_file.parent.mkdir(parents=True,exist_ok=True)
  data_file.write_text(json.dumps(tasks,ensure_ascii=False,indent=2),encoding="utf-8")

def show_add_form(tasks):
  st.subheader("Новая задача")
  with st.form("add_task",clear_on_submit=True):
    title=st.text_input("Название",max_chars=120,placeholder="Например ,помыть посуду")
    left,right=st.columns(2)
    category=left.selectbox("Категоря",categories)
    due=right.date_input("Срок",value=None,format="DD.MM.YYYY")
    submitted=st.form_submit_button("Добавить задачу"),type="primary")
  if submitted:
    if not title.strip():
      st.warning("Введите название")
      return 
    task={
      "id": uuid4().hex,
      "title": title.strip(),
      "category": category,
      "due":due.isoformat() if due else None,
      "completed_on": None,
    }
    save_tasks([*tasks,task])
    st.rerun()

def show_tasks_tab():
  tasks=load_tasks()
  show_add_form(tasks)
  st.subheader("Список задачь")
  if not tasks:
    st.caption("Добавте задачу")
    return 
  for task in tasks:
    st.text(f"{task["title"]} | {task["category"]} | {task["due"] or "без срока"})
  
 
st.set_page_config(page_title="журнал задач",page_icon="📋",layout="centered")
st.title("журнал задач")
#st.caption("здесь будут задачи")

tasks_tab,=st.tabs(["задачи"])
with tasks_tab:
  #st.write("скоро cписок задач")
  #if st.button("нажми"):
    #st.write("=)")

  show_tasks_tab()
  
