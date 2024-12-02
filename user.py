from space import view_available_spaces, book_space, view_booking_history, filter_spaces, sort_spaces, format_spaces, cancel_booking, spaces
from utilis import safe_input

def user_menu(current_user):
    def view_spaces():
        available_spaces = view_available_spaces()
        format_spaces(available_spaces)

    def book_space():
        space_id = int(safe_input("Введите ID помещения: ", lambda x: x.isdigit(), "Пожалуйста, введите число."))
        book_space(current_user, space_id)

    def view_history():
        view_booking_history(current_user)

    def sort_spaces():
        key = safe_input("Введите критерий сортировки (price, rating): ", lambda x: x in ['price', 'rating'], "Пожалуйста, введите 'price' или 'rating'.")
        reverse = safe_input("Сортировать по убыванию? (y/n): ", lambda x: x in ['y', 'n'], "Пожалуйста, введите 'y' или 'n'.") == 'y'
        sorted_spaces = sort_spaces(lambda space: space[key], reverse)
        format_spaces(sorted_spaces)

    def filter_spaces():
        min_price = int(safe_input("Введите минимальную цену: ", lambda x: x.isdigit(), "Пожалуйста, введите число."))
        max_price = int(safe_input("Введите максимальную цену: ", lambda x: x.isdigit(), "Пожалуйста, введите число."))
        criteria = lambda space: min_price <= space['price'] <= max_price
        filtered_spaces = filter_spaces(criteria)
        format_spaces(filtered_spaces)


    def cancel_booking():
        space_id = int(safe_input("Введите ID помещения: ", lambda x: x.isdigit(), "Пожалуйста, введите число."))
        cancel_booking(current_user, space_id)

    def logout():
        nonlocal running
        running = False

    actions = {
        1: view_spaces,
        2: book_space,
        3: view_history,
        4: sort_spaces,
        5: filter_spaces,
        6: cancel_booking,
        7: logout
    }

    running = True
    while running:
        print(f"Добро пожаловать, {current_user['username']}!")
        print("1. Просмотр доступных помещений")
        print("2. Бронирование помещения")
        print("3. Просмотр истории бронирований")
        print("4. Сортировка помещений")
        print("5. Фильтрация помещений")
        print("6. Отмена бронирования")
        print("7. Выйти из аккаунта")

        choice = int(safe_input("Выберите действие: ", lambda x: x.isdigit(), "Пожалуйста, введите число."))
        action = actions.get(choice, lambda: print("Неверный выбор"))
        action()