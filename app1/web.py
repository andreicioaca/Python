import streamlit as st
import functions as f


todos = f.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    f.push_todos(todos)


st.title("Ordine de la Victoria")
st.subheader("Scrii aici ce trebuie sa facem")
st.write("aplicatia asta e facuta sa ne creasca productivitatea")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        f.push_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Adauga un ordin...",
              on_change=add_todo, key='new_todo')

