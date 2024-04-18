# Функция для отображения списка дел
def show_todo_list():
    try:
        with open("todo.txt", "r") as file:
            todo_list = file.readlines()
            if not todo_list:
                print("Список дел пуст")
            else:
                print("Список дел:")
                for index, task in enumerate(todo_list, 1):
                    print(f"{index}. {task.strip()}")
    except FileNotFoundError:
        print("Файл todo.txt не найден.")


# Функция для добавления нового дела
def add_task():
    task = input("Введите новое дело: ")
    with open("todo.txt", "a") as file:
        file.write(task + "\n")
    print("Дело добавлено в список.")


# Функция для редактирования дела
def edit_task():
    try:
        with open("todo.txt", "r") as file:
            todo_list = file.readlines()
            if not todo_list:
                print("Список дел пуст")
                return
            print("Список дел:")
            for index, task in enumerate(todo_list, 1):
                print(f"{index}. {task.strip()}")
            choice = int(input("Введите номер дела, которое хотите отредактировать: "))
            if 1 <= choice <= len(todo_list):
                new_task = input("Введите новое описание дела: ")
                todo_list[choice - 1] = new_task + "\n"
                with open("todo.txt", "w") as file:
                    file.writelines(todo_list)
                print("Дело успешно отредактировано.")
            else:
                print("Неверный номер дела.")
    except FileNotFoundError:
        print("Файл todo.txt не найден.")
    except ValueError:
        print("Пожалуйста, введите номер дела цифрой.")


# Функция для удаления дела
def delete_task():
    try:
        with open("todo.txt", "r") as file:
            todo_list = file.readlines()
            if not todo_list:
                print("Список дел пуст")
                return
            print("Список дел:")
            for index, task in enumerate(todo_list, 1):
                print(f"{index}. {task.strip()}")
            choice = int(input("Введите номер дела, которое хотите удалить: "))
            if 1 <= choice <= len(todo_list):
                del todo_list[choice - 1]
                with open("todo.txt", "w") as file:
                    file.writelines(todo_list)
                print("Дело успешно удалено.")
            else:
                print("Неверный номер дела.")
    except FileNotFoundError:
        print("Файл todo.txt не найден.")
    except ValueError:
        print("Пожалуйста, введите номер дела цифрой.")


# Основная функция программы
def main():
    while True:
        print("\nМеню:")
        print("1. Показать мой список дел")
        print("2. Добавить дело")
        print("3. Отредактировать дело")
        print("4. Удалить дело")
        print("0. Закрыть")

        choice = input("Выберите действие: ")

        if choice == "1":
            show_todo_list()
        elif choice == "2":
            add_task()
        elif choice == "3":
            edit_task()
        elif choice == "4":
            delete_task()
        elif choice == "0":
            print("Программа закрыта.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите из списка.")


if __name__ == "__main__":
    main()

