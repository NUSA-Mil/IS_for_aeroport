users = [
    {'username': 'user1', 'password': 'password1', 'role': 'user', 'subscription_type': 'Standard', 'history': [], 'created_at': '2024-01-01'},
    {'username': 'admin', 'password': 'adminpassword', 'role': 'admin', 'created_at': '2024-01-01'}
]

def create_user(username, password, role):
    new_user = {
        'username': username,
        'password': password,
        'role': role,
        'created_at': '2024-12-01',
        'history': []  # Добавьте историю для новых пользователей
    }
    users.append(new_user)
    print(f"Пользователь {username} успешно создан")

def delete_user(username):
    global users
    users = [user for user in users if user['username'] != username]
    print(f"Пользователь {username} успешно удален")

def edit_user(username, new_password=None, new_role=None):
    for user in users:
        if user['username'] == username:
            if new_password:
                user['password'] = new_password
            if new_role:
                user['role'] = new_role
            print(f"Пользователь {username} успешно обновлен")
            return
    print("Пользователь не найден")
