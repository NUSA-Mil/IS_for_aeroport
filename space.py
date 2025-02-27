class Space:
    def __init__(self, id, name, price, rating, area):
        self.id = id
        self.name = name
        self.price = price
        self.rating = rating
        self.area = area
        self.availability = True

class SpaceManager:
    def __init__(self):
        self.spaces = [
            Space(1, 'Помещение A', 5000, 4.5, 100),
            Space(2, 'Помещение B', 7000, 4.8, 150)
        ]

    def view_available_spaces(self):
        available_spaces = [space for space in self.spaces if space.availability]
        if not available_spaces:
            print("Нет доступных помещений.")
        else:
            for space in available_spaces:
                print(f"ID: {space.id}, Название: {space.name}, Цена: {space.price}, Рейтинг: {space.rating}, Площадь: {space.area} м²")

    def book_space(self, user, space_id):
        for space in self.spaces:
            if space.id == space_id and space.availability:
                space.availability = False
                user.history.append(space.name)
                print(f"Вы успешно забронировали {space.name}")
                return
        print("Невозможно забронировать помещение.")

    def cancel_booking(self, user, space_id):
        for space in self.spaces:
            if space.id == space_id and space.name in user.history:
                space.availability = True
                user.history.remove(space.name)
                print(f"Бронь помещения {space.name} успешно отменена")
                return
        print("Невозможно отменить бронь.")

    def filter_spaces(self, min_price, max_price):
        filtered_spaces = [space for space in self.spaces if min_price <= space.price <= max_price]
        return filtered_spaces

    def sort_spaces(self, key, reverse=False):
        valid_keys = ['name', 'price', 'rating', 'area']
        if key not in valid_keys:
            print("Неверный ключ для сортировки.")
            return self.spaces  # Возвращаем исходный список, если ключ неверный
        return sorted(self.spaces, key=lambda space: getattr(space, key), reverse=reverse)
