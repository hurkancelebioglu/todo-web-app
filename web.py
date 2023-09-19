import streamlit as st
import functions


def add_todo():
    todo_loc = st.session_state["new_todo"] + "\n"
    todos.append(todo_loc)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""


def completed_todos():
    """remove items to be deleted from todos and return list of items to be deleted"""
    del_key_list = []

    global todos
    #  use copy of reversed list for popping during iteration
    todos_copy = todos[:]
    todos_copy.reverse()
    # get length todos for pop
    list_len = len(todos)

    # recreate the key names
    for INDEX, TODO in enumerate(todos):
        # if cb is ticked, store key and pop corresponding todo_
        if st.session_state[f"cb_{INDEX}"]:
            del_key_list.append(f"cb_{INDEX}")
            todos_copy.pop(list_len - (INDEX + 1))

    # write the updated todos_copy todos text file
    functions.write_todos(reversed(todos_copy))

    return del_key_list


todos = functions.get_todos()

st.title("2Do")
st.subheader("Minimalistic todo app.")
st.write('This app is to increase your <font color="blue">productivity</font>.',
         unsafe_allow_html=True)

for index, todo in enumerate(todos):
    # prevent identical keys for double entries
    checkbox = st.checkbox(todo, key=f"cb_{index}")

st.text_input(label="Add a todo", label_visibility="hidden",
              placeholder="Add a new todo...",
              on_change=add_todo, key="new_todo")

# add button "Completed"
st.button("**Complete**", key="completed_todo")

# if button "del completed" is clicked
if st.session_state["completed_todo"]:

    del_todos = completed_todos()

    if del_todos:
        for item in del_todos:
            del st.session_state[item]
