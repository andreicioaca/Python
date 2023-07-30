def get_todos(filepath='todos.txt'):
    """Read a text file and return the list of to_do items"""
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def push_todos(todos_arg, filepath='todos.txt'):
    """Write a to_do items in the text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
