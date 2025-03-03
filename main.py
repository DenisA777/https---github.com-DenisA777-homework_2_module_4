def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:

            salaries_sum = 0

            for line in file:

                try:
                    name, salary = line.strip().split(',')
                    salaries_sum += float(salary)

                except ValueError:
                    print("Помилка при обробці рядка")
                    continue

            average_salary = salaries_sum / 3

            return salaries_sum, average_salary

    except FileNotFoundError:
        print('Файл не знайдено')
        return -1, -1


total, average = total_salary("text")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")




def get_cats_info(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:

            cats_data = []

            for line in file:
                try:
                    cats_id, name, age = line.strip().split(',')
                    cat_info = {'id': cats_id, 'name': name, 'age': age}

                    cats_data.append(cat_info)


                except ValueError:
                    print("Помилка при обробці рядка")
                    continue

            return cats_data

    except FileNotFoundError:
        print('Файл не знайдено')
        return -1, -1


cats_info = get_cats_info("cats_file")
print(cats_info)





contacts = {}

def parse_input(user_input):
    command, *args = user_input.split()

    command = command.strip().lower()
    return command, args


def add_contact(item):

    if len(item) != 2:
        return "Помилка: використовуйте 'add [ім'я] [номер телефону]'"

    name, phone = item
    contacts[name] = phone
    return "Contact added."

def change_contact(item):

    if len(item) != 2:
        return "Помилка: використовуйте 'change [ім'я] [новий номер]'"
    name, phone = item

    if name in contacts:
        contacts[name] = phone
        return "Contact updated."

    return "Помилка: контакт не знайдено."


def show_phone(item):

    if len(item) != 1:
        return "Помилка: використовуйте 'phone [ім'я]'"

    name = item[0]
    return contacts.get(name, "Помилка: контакт не знайдено.")

def show_all():

    if not contacts:
        return "Список контактів порожній!"

    result = []
    for name, phone in contacts.items():
        result.append(f"{name} {phone}")

    return '\n'.join(result)


def main():

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ").strip()
        if not user_input:
            continue

        command, item = parse_input(user_input)

        if command in ["exit", "close"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(item))
        elif command == "change":
            print(change_contact(item))
        elif command == "phone":
            print(show_phone(item))
        elif command == "all":
            print(show_all())
        else:
            print("Invalid command")
            

main()