import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo_new=st.session_state['new_item']+"\n"
    todos.append(todo_new)
    functions.write_todos(todos)


st.title("My Todos App")
st.subheader("This is my app")
st.write("This app is to increase your productivity")

for i, todo in enumerate(todos):
    checkbox_key = f"todo_{i}"  # Generate a unique key for each checkbox
    checkbox=st.checkbox(todo, key=checkbox_key)
    if checkbox:
        todos.pop(i)
        functions.write_todos(todos)
        st.experimental_rerun()

new_todo = st.text_input(label="my todo", placeholder="Add new todo...",
                         on_change=add_todo,key="new_item")  # Use a unique key for the text_input
