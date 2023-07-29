todos = []

while True:
    user_action = input("add or show or exit or edit: ")
    user_action = user_action.strip()

    if user_action == 'add':
        todo = input("enter a todo: ")
        todos.append(todo)
    elif user_action == 'show':
        for index,item in enumerate(todos):
            print(index + 1, '-',  item)
    elif user_action == 'edit':
        number = int(input("Number of the todo to edit: "))
        number = number - 1
        new_todo = input("edit the todo: ")
        todos[number] = new_todo
    elif user_action == 'complete':
        number = int(input("Number of the todo to complete: "))
        number = number - 1
        todos.pop(number)
    elif user_action == 'exit':
        break
print('Byeee')




