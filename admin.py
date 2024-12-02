from space import add_space, remove_space, edit_space, spaces
from utilis import safe_input
from user_manager import create_user, delete_user, edit_user, users  # Добавьте импорт пользователей


def analyze_statistics():
    total_bookings = sum([len(user['history']) for user in users if user['role'] == 'user'])

    booked_spaces = [space for space in spaces if not space['availability']]
    if booked_spaces:
        avg_cost = sum([space['price'] for space in booked_spaces]) / len(booked_spaces)
        print(f"Общее количество бронирований: {total_bookings}")
        print(f"Средняя стоимость бронирований: {avg_cost:.2f}")
    else:
        print("Данных нет")


def admin_menu():
    def add_space():
        id = int(safe_input("Введите ID: ", lambda x: x.isdigit(), "Пожалуйста, введите число."))
        name = safe_input("Введите название: ", lambda x: len(x) > 0, "Пожалуйста, введите название.")
        price = int(safe_input("Введите цену: ", lambda x: x.isdigit(), "Пожалуйста, введите число."))
        rating = float(
            safe_input("Введите рейтинг: ", lambda x: x.replace('.', '', 1).isdigit(), "Пожалуйста, введите число."))
        add_space(id, name, price, rating)

    def remove_space():
        space_id = int(safe_input("Введите ID помещения: ", lambda x: x.isdigit(), "Пожалуйста, введите число."))
        remove_space(space_id)

    def edit_space():
        space_id = int(safe_input("Введите ID помещения: ", lambda x: x.isdigit(), "Пожалуйста, введите число."))
        name = input("Введите новое название (или оставьте пустым): ")
        price = input("Введите новую цену (или оставьте пустым): ")
        rating = input("Введите новый рейтинг (или оставьте пустым): ")
        edit_space(space_id, name if name else None, int(price) if price else None, float(rating) if rating else None)

    def view_statistics():
        analyze_statistics()

    def create_user():
        username = safe_input("Введите имя пользователя: ", lambda x: len(x) > 0,
                              "Пожалуйста, введите имя пользователя.")
        password = safe_input("Введите пароль: ", lambda x: len(x) > 0, "Пожалуйста, введите пароль.")
        role = safe_input("Введите роль (user/admin): ", lambda x: x in ['user', 'admin'],
                          "Пожалуйста, введите 'user' или 'admin'.")
        create_user(username, password, role)

    def delete_user():
        username = safe_input("Введите имя пользователя для удаления: ", lambda x: len(x) > 0,
                              "Пожалуйста, введите имя пользователя.")
        delete_user(username)

    def edit_user():
        username = safe_input("Введите имя пользователя для редактирования: ", lambda x: len(x) > 0,
                              "Пожалуйста, введите имя пользователя.")
        new_password = input("Введите новый пароль (или оставьте пустым): ")
        new_role = input("Введите новую роль (или оставьте пустым): ")
        edit_user(username, new_password if new_password else None, new_role if new_role else None)

    def logout():
        nonlocal running
        running = False

    actions = {
        1: add_space,
        2: remove_space,
        3: edit_space,
        4: view_statistics,
        5: create_user,
        6: delete_user,
        7: edit_user,
        8: logout
    }

    running = True
    while running:
        print("1. Добавить помещение")
        print("2. Удалить помещение")
        print("3. Редактировать помещение")
        print("4. Просмотр и анализ статистики")
        print("5. Создать пользователя")
        print("6. Удалить пользователя")
        print("7. Редактировать пользователя")
        print("8. Выйти из аккаунта")

        choice = int(safe_input("Выберите действие: ", lambda x: x.isdigit(), "Пожалуйста, введите число."))
        action = actions.get(choice, lambda: print("Неверный выбор"))
        action()