from user import user_menu
from admin import admin_menu
from user_manager import create_user, delete_user, edit_user, users
def main():
    while True:
        current_user = None

        while not current_user:
            print("Добро пожаловать! Пожалуйста, авторизуйтесь.")
            username = input("Логин: ")
            password = input("Пароль: ")

            for user in users:
                if user['username'] == username and user['password'] == password:
                    current_user = user
                    break

            if not current_user:
                print("Неверный логин или пароль. Попробуйте снова.")

        if current_user['role'] == 'user':
            user_menu(current_user)
        elif current_user['role'] == 'admin':
            admin_menu()

if __name__ == "__main__":
    main()