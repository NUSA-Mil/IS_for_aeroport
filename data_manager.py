import csv

class DataManager:
    def __init__(self, user_manager):
        self.user_manager = user_manager

    def export_users(self, filename='users.csv'):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Username', 'Password', 'Role'])
            for user in self.user_manager.users:
                writer.writerow([user.username, user.password, user.role])
        print(f"Данные пользователей экспортированы в {filename}.")

    def import_users(self, filename='users.csv'):
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Пропускаем заголовок
            for row in reader:
                if len(row) < 3:  # Проверка на количество элементов
                    print(f"Пропущена строка: {row} - недостаточно данных.")
                    continue
                username, password, role = row
                self.user_manager.create_user(username, password)
        print(f"Данные пользователей импортированы из {filename}.")
