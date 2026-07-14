import streamlit as st
from core.add_task import add_task
from core.view_tasks import view_tasks
from core.delete_task import delete_task

if "tasks" not in st.session_state:
    st.session_state.tasks = []

st.title("To-Do List")

tab1, tab2, tab3 = st.tabs(["Add Task", "View Tasks", "Delete Task"])

with tab1:
    st.write("Hi! what is on your agenda?")
    task_name = st.text_input("Task Name")
    task_description = st.text_input("Task Description")
    task_due_date = st.date_input("Task Due Date")
    task_priority = st.selectbox("Task Priority", ["Low", "Medium", "High"])
    task_status = st.selectbox("Task Status", ["Pending", "Completed"])

    if st.button("Add Task"):
        add_task(
            st.session_state.tasks,
            task_name,
            task_description,
            str(task_due_date),
            task_priority,
            task_status,
        )
        st.success("Task added!")

with tab2:
    st.write("Here are your tasks:")
    tasks = view_tasks(st.session_state.tasks)
    if tasks:
        for task in tasks:
            st.write(task)
    else:
        st.write("No tasks yet.")

with tab3:
    task_to_delete = st.text_input("Task name to delete")
    if st.button("Delete Task"):
        if delete_task(task_to_delete, st.session_state.tasks):
            st.success(f"Task '{task_to_delete}' deleted!")
        else:
            st.error(f"Task '{task_to_delete}' not found.")
