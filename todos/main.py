def read_todos(filepath):
    with open(filepath, 'r') as local_file:
        local_todos = local_file.readlines()
    return local_todos


def write_todos(filepath, todos_arg):
    with open(filepath, 'w') as local_file:
        local_file.writelines(todos_arg)


while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        """
        file = open('files/todos.txt', 'r')
        todos = file.readlines()
        file.close()
        """
        todos = read_todos("files/todos.txt")

        todos.append(todo + '\n')

        # with open('files/todos.txt', 'w') as file:
        #     file.writelines(todos)
        write_todos("files/todos.txt", todos)

    elif user_action.startswith("show"):
        todos = read_todos("files/todos.txt")
        """
        new_todos = []
        for item in todos:
            todo = item.strip('\n')
            new_todos.append(todo)

        new_todos = [item.strip('\n') for item in todos]
        """
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number -= 1

            todos = read_todos("files/todos.txt")

            # todos.__setitem__(number, input("Enter a new todo: "))
            todos[number] = input("Enter a new todo: ") + '\n'
            write_todos("files/todos.txt", todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            index = number - 1

            todos = read_todos("files/todos.txt")

            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos("files/todos.txt", todos)
            message = f'Todo {todo_to_remove} was removed from the list'
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid.")
print("Bye!")

