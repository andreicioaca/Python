from tkinter import font

import functions as f
import PySimpleGUI as p

label = p.Text("Type in a to-do")
input_box = p.InputText(tooltip="Enter todo", key="todo")
add_button = p.Button("Add")
list_box =p.Listbox(values=f.get_todos(), key="todos",
                    enable_events=True, size=[45, 10])
edit_button = p.Button('Edit')
complete_button = p.Button('Done')
exit_button = p.Button('Exit')

window = p.Window('My To-do App',
                  layout=[[label],
                         [input_box, add_button],
                         [list_box, edit_button, complete_button],
                         [exit_button]],
                  font=('Helvetica', 20))
while True:
    event, values = window.read()
    print(1, event)
    print(2, values)

    if event == "Add":

        todos = f.get_todos()
        new_todo = values['todo'] + '\n'
        todos.append(new_todo)
        f.push_todos(todos)
        window['todos'].update(values=todos)

    elif event == "Edit":

        todo_to_edit = values['todos'][0]
        new_todo = values['todo']

        todos = f.get_todos()
        index = todos.index(todo_to_edit)
        todos[index] = new_todo
        f.push_todos(todos)
        window['todos'].update(values=todos)

    elif event == 'Done':

        todo_to_complete = values['todos'][0]
        todos = f.get_todos()
        todos.remove(todo_to_complete)
        f.push_todos(todos)
        window['todos'].update(values=todos)
        window['todo'].update(value='')

    elif event == 'Exit':
        break

    elif event == 'todos':

        window['todo'].update(value=values['todos'][0])


    elif event == p.WIN_CLOSED:
        break

window.close()


