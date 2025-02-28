from data_manager import DataManager
from user import BaseUser
from space import SpaceManager, Space

class Admin(BaseUser):
    def __init__(self, user_manager):
        super().__init__('admin', 'adminpassword', role='admin')  # Указываем роль
        self.data_manager = DataManager(user_manager)
        self.user_manager = user_manager
        self.space_manager = SpaceManager()

    def admin_menu(self):
        actions = {
            1: self.add_space,
            2: self.remove_space,
            3: self.edit_space,
            4: self.view_statistics,
            5: self.create_user_action,
            6: self.delete_user_action,
            7: self.edit_user_action,
            8: self.logout,
            9: self.export_users,
            10: self.import_users
        }

        while True:
            print("1. Добавить помещение")
            print("2. Удалить помещение")
            print("3. Редактировать помещение")
            print("4. Просмотр и анализ статистики")
            print("5. Создать пользователя")
            print("6. Удалить пользователя")
            print("7. Редактировать пользователя")
            print("8. Выход из аккаунта")
            print("9. Экспортировать пользователей")
            print("10. Импортировать пользователей")
            choice = int(input("Выберите действие: "))

            action = actions.get(choice)
            if action:
                if action() is False:
                    break
            else:
                print("Неверный выбор")

    def export_users(self):
        if self.data_manager:
            self.data_manager.export_users()
        else:
            print("DataManager не инициализирован.")

    def import_users(self):
        if self.data_manager:
            self.data_manager.import_users()
        else:
            print("DataManager не инициализирован.")

    def add_space(self):
        name = input("Введите название помещения: ")
        price = float(input("Введите цену помещения: "))
        rating = float(input("Введите рейтинг помещения: "))
        area = float(input("Введите площадь помещения: "))
        new_space = Space(len(self.space_manager.spaces) + 1, name, price, rating, area)
        self.space_manager.spaces.append(new_space)
        print(f"Помещение '{name}' успешно добавлено.")

    def remove_space(self):
        space_id = int(input("Введите ID помещения для удаления: "))
        self.space_manager.spaces = [space for space in self.space_manager.spaces if space.id != space_id]
        print(f"Помещение с ID {space_id} успешно удалено.")

    def edit_space(self):
        space_id = int(input("Введите ID помещения для редактирования: "))
        for space in self.space_manager.spaces:
            if space.id == space_id:
                space.name = input("Введите новое название помещения: ")
                space.price = float(input("Введите новую цену помещения: "))
                space.rating = float(input("Введите новый рейтинг помещения: "))
                space.area = float(input("Введите новую площадь помещения: "))
                print(f"Помещение с ID {space_id} успешно обновлено.")
                return
        print("Помещение не найдено.")

    def view_statistics(self):
        total_spaces = len(self.space_manager.spaces)
        available_spaces = len([space for space in self.space_manager.spaces if space.availability])
        print(f"Всего помещений: {total_spaces}")
        print(f"Доступных помещений: {available_spaces}")

    def create_user_action(self):
        username = input("Введите имя пользователя: ")
        password = input("Введите пароль: ")
        role = input("Введите роль (user/admin): ")
        self.user_manager.create_user(username, password)

    def delete_user_action(self):
        username = input("Введите имя пользователя для удаления: ")
        self.user_manager.delete_user(username)

    def edit_user_action(self):
        username = input("Введите имя пользователя для редактирования: ")
        new_password = input("Введите новый пароль (оставьте пустым, если не хотите менять): ")
        new_role = input("Введите новую роль (оставьте пустым, если не хотите менять): ")
        self.user_manager.edit_user(username, new_password if new_password else None, new_role if new_role else None)

    def logout(self):
        print(f"{self.username} вышел из системы.")
        return False


