import functions as f
import PySimpleGUI as p

label = p.Text("Type in a to-do")
input_box = p.InputText(tooltip="Enter todo")
add_button = p.Button("Add")

window = p.Window('My To-do App', layout=[[label], [add_button, input_box]])
window.read()
window.close()


