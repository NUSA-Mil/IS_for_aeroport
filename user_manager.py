from admin import Admin
from user import User

class UserManager:
    def __init__(self):
        self.users = [
            User('user1', 'password1'),
            Admin(self)  # Создаем администратора
        ]

    def authenticate(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                return user
        return None

    def create_user(self, username, password, role='user'):
        if role == 'admin':
            new_user = Admin(self)  # Создаем администратора
        else:
            new_user = User(username, password)  # Создаем обычного пользователя
        self.users.append(new_user)
        print(f"Пользователь {username} успешно создан с ролью '{role}'.")

    def delete_user(self, username):
        self.users = [user for user in self.users if user.username != username]
        print(f"Пользователь {username} успешно удален.")

    def edit_user(self, username, new_password=None, new_role=None):
        for user in self.users:
            if user.username == username:
                if new_password:
                    user.password = new_password
                if new_role:
                    user.role = new_role  # Убедитесь, что атрибут role существует у класса User
                print(f"Пользователь {username} успешно обновлен.")
                return
        print("Пользователь не найден.")
