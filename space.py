spaces = [
    {'id': 1, 'name': 'Помещение A', 'price': 5000, 'availability': True, 'rating': 4.5, 'added_at': '2024-01-01'},
    {'id': 2, 'name': 'Помещение B', 'price': 7000, 'availability': True, 'rating': 4.8, 'added_at': '2024-02-01'}
]
def view_available_spaces():
    available_spaces = [space for space in spaces if space['availability']]
    return available_spaces

def book_space(user, space_id):
    for space in spaces:
        if space['id'] == space_id and space['availability']:
            space['availability'] = False
            user['history'].append(space['name'])
            print(f"Вы успешно забронировали {space['name']}")
            return
    print("Невозможно забронировать помещение")

def view_booking_history(user):
    if user['history']:
        print("Ваша история бронирований:", ", ".join(user['history']))
    else:
        print("История бронирований пуста")

def add_space(id, name, price, rating):
    new_space = {
        'id': id,
        'name': name,
        'price': price,
        'availability': True,
        'rating': rating,
        'added_at': '2024-12-01'
    }
    spaces.append(new_space)
    print(f"Помещение {name} успешно добавлено")

def remove_space(space_id):
    global spaces
    spaces = [space for space in spaces if space['id'] != space_id]
    print(f"Помещение с ID {space_id} успешно удалено")

def edit_space(space_id, name=None, price=None, rating=None):
    for space in spaces:
        if space['id'] == space_id:
            if name:
                space['name'] = name
            if price:
                space['price'] = price
            if rating:
                space['rating'] = rating
            print(f"Помещение с ID {space_id} успешно обновлено")
            return
    print("Помещение не найдено")
def filter_spaces(criteria):
    return list(filter(criteria, spaces))

def sort_spaces(key, reverse=False):
    return sorted(spaces, key=key, reverse=reverse)

def format_spaces(spaces):
    if not spaces:
        print("Нет доступных помещений.")
    else:
        for space in spaces:
            print(f"ID: {space['id']}, Название: {space['name']}, Цена: {space['price']}, Рейтинг: {space['rating']}, Доступность: {'Да' if space['availability'] else 'Нет'}")

def cancel_booking(user, space_id):
    for space in spaces:
        if space['id'] == space_id and space['name'] in user['history']:
            space['availability'] = True
            user['history'].remove(space['name'])
            print(f"Бронь помещения {space['name']} успешно отменена")
            return
    print("Невозможно отменить бронь. Либо помещение не забронировано, либо неверный ID.")
