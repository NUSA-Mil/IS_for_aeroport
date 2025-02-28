from user import User
from user_manager import UserManager
from data_manager import DataManager
from admin import Admin

def main():
    user_manager = UserManager()
    data_manager = DataManager(user_manager)

    # Передаем data_manager в Admin
    admin = Admin(user_manager)
    admin.data_manager = data_manager  # Добавляем ссылку на data_manager

    while True:
        current_user = None
        while not current_user:
            print("Добро пожаловать! Пожалуйста, авторизуйтесь.")
            username = input("Логин: ")
            password = input("Пароль: ")
            current_user = user_manager.authenticate(username, password)

            if not current_user:
                print("Неверный логин или пароль. Попробуйте снова.")

        if isinstance(current_user, User):
            current_user.user_menu(user_manager)
        elif isinstance(current_user, Admin):
            current_user.admin_menu()

if __name__ == "__main__":
    main()
