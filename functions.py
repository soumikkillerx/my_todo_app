filename='files/todos.txt'
def get_todos(filename='files/todos.txt'):
    file = open(filename, 'r')
    todos = file.readlines()
    file.close()
    return todos


def write_todos(todos,filename='files/todos.txt'):
    file = open(filename, 'w')
    file.writelines(todos)
    file.close()
