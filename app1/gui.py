import functions as f
import PySimpleGUI as p

label = p.Text("Type in a to-do")

window = p.Window('My To-do App', layout=[""])
window.read()
window.close()


