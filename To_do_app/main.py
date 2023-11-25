
def get_todos(path_to_file='todos.txt'):
    with open(path_to_file, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_inp, path_to_file='todos.txt'):
    with open(path_to_file, 'w') as file:
        file.writelines(todos_inp)


while True:
    todo = input("Type add, show, edit, delete or exit: ").strip()
    # if 'add' not in string or 'new' in string:
    if todo.startswith("add"):
        user_prompt = todo[4:] + '\n'
        todos = get_todos()
        todos.append(user_prompt)
        print(todos)
        write_todos(todos)
    elif todo.startswith("show"):
        # another way to do that is:
        # new todos = [item.strip('\n') for item in todos]
        todos = get_todos()
        for i, item in enumerate(todos):
            print(f"{i+1}-{item.rstrip()}")
    elif todo.startswith("exit"):
        break
    elif todo.startswith("edit"):
        todos = get_todos()
        print(f"Here is todos existing:{todos}")

        number = int(input("What number should be edited?:"))
        user_prompt = input("Enter a todo:")
        todos[number - 1] = user_prompt + '\n'

        write_todos(todos)
    elif todo.startswith("delete"):
        todos = get_todos()
        print(f"Here is todos existing:{todos}")

        number = int(input("What number should be deleted?:"))
        try:
            del todos[number - 1]
            write_todos(todos)
        except IndexError:
            print("There is no item with that number.")
            continue
    else:
        print("Try one more time!")

print("Bye!")
