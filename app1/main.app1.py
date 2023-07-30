import functions as f
import time as t

now = t.strftime("%d %b, %H:%M")
print('it is:', now)


while True:
    user_action = input("add or show or exit or edit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):

        todo = user_action[4:]

        todos = f.get_todos()

        todos.append(todo + '\n')

        f.push_todos(todos)

    elif user_action.startswith('show'):

        todos = f.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(index + 1, '-',  item)

    elif user_action.startswith('edit'):

        try:
            number = int(user_action[5:])
            number = number - 1

            todos = f.get_todos()

            new_todo = input("edit the todo: ")
            todos[number] = new_todo + '\n'

            f.push_todos(todos)

        except ValueError:
            print('command not valid')
            continue
    elif user_action.startswith('complete'):

        try:
            number = int(user_action[9:])

            todos = f.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            f.push_todos(todos)

            mess = f"Todo: ___{todo_to_remove}___ was removed from the list"
            print(mess)
        except IndexError:
            print('there is no item with this number')
            continue

    elif user_action == 'exit':
        break

    else:
        print('command not valid')

print('Byeee')
