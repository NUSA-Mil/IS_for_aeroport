from space import SpaceManager

class BaseUser:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def logout(self):
        print(f"{self.username} вышел из системы.")
        return False

class User(BaseUser):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.role = 'user'
        self.history = []

    def user_menu(self, user_manager):
        space_manager = SpaceManager()  # Инициализируем SpaceManager здесь
        actions = {
            1: space_manager.view_available_spaces,
            2: lambda: self.book_space_action(space_manager),  # Передаем space_manager
            3: self.view_history,
            4: lambda: self.sort_spaces_action(space_manager),  # Исправлено
            5: lambda: self.filter_spaces_action(space_manager),  # Исправлено
            6: lambda: self.cancel_booking_action(space_manager),  # Передаем space_manager
            7: self.logout
        }

        while True:
            print(f"Добро пожаловать, {self.username}!")
            print("1. Просмотр доступных помещений")
            print("2. Бронирование помещения")
            print("3. Просмотр истории бронирований")
            print("4. Сортировка помещений")
            print("5. Фильтрация помещений")
            print("6. Отмена бронирования")
            print("7. Выйти из аккаунта")
            choice = int(input("Выберите действие: "))
            action = actions.get(choice, lambda: print("Неверный выбор"))
            if action() is False:  # Если logout вернул False, выходим из меню
                break

    def book_space_action(self, space_manager):
        space_id = int(input("Введите ID помещения для бронирования: "))
        space_manager.book_space(self, space_id)  # Передаем текущего пользователя

    def cancel_booking_action(self, space_manager):
        space_id = int(input("Введите ID помещения для отмены бронирования: "))
        space_manager.cancel_booking(self, space_id)  # Передаем текущего пользователя

    def view_history(self):
        if self.history:
            print("Ваша история бронирований:", ", ".join(self.history))
        else:
            print("История бронирований пуста.")

    def sort_spaces_action(self, space_manager):
        key = input("Введите ключ для сортировки (name, price, rating, area): ")
        order = input("Сортировать по убыванию? (yes/no): ").strip().lower() == 'yes'
        sorted_spaces = space_manager.sort_spaces(key, reverse=order)
        for space in sorted_spaces:
            print(f"ID: {space.id}, Название: {space.name}, Цена: {space.price}, Рейтинг: {space.rating}, Площадь: {space.area} м²")

    def filter_spaces_action(self, space_manager):
        min_price = float(input("Введите минимальную цену: "))
        max_price = float(input("Введите максимальную цену: "))
        filtered_spaces = space_manager.filter_spaces(min_price, max_price)
        if filtered_spaces:
            for space in filtered_spaces:
                print(f"ID: {space.id}, Название: {space.name}, Цена: {space.price}, Рейтинг: {space.rating}, Площадь: {space.area} м²")
        else:
            print("Нет помещений, соответствующих вашим критериям.")
