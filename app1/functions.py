FILEPATH = "D:\\Python\\app1\\todos.txt"


def get_todos(filepath=FILEPATH):
    """Read a text file and return the list of to_do items"""
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def push_todos(todos_arg, filepath=FILEPATH):
    """Write a to_do items in the text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)






if __name__ == "__main__":
    print("Hello")
    print(get_todos())
