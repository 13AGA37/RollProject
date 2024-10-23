import os


class RollController:
    """Класс RollController управляет взаимодействием между моделью и представлением"""

    def __init__(self, model):
        """Конструктор, который запускается при создании объекта класса RollModel."""
        self.model = model # Сохраняем экземпляр модели

    def get_restaurant_menu(self): # Получаем представление меню ресторана
        """Способ отправки информации для меню в ресторане."""
        roll_data = (f'Ролл :: {self.model.get_name()}\n'
                      f'Цена :: {self.model.get_price()}\n'
                      f'Вес :: {self.model.get_weight()}\n'
                      f'Состав :: {", ".join(self.model.get_ingredients())}\n')
        return roll_data # Возвращаем строку меню # Получаем представление меню сайта

    def get_site_menu(self):
        """Способ передачи информации для формирования меню на веб-странице."""
        roll_data = (f'Ролл :: {self.model.get_name()}\n'
                      f'Цена :: {self.model.get_price()}\n'
                      f'Вес :: {self.model.get_weight()}\n'
                      f'Состав :: {", ".join(self.model.get_ingredients())}\n'
                      f'Фото ::{os.startfile(self.model.get_picture())}')  # Открываем файл изображения return roll_data  # Возвращаем строку меню
        return roll_data

        """Функции set_ingredients, set_price, set_weight и set_picture служат для передачи информации от представления к модели.
        Они проверяют права доступа пользователя и тип данных.
        Если права доступа подходят, то данные отправляются в модель. Если нет, то выводится сообщение об ошибке."""
    def set_ingredients(self, user_rights, new_ingredients):
        if user_rights in ['Admin', 'IsStaff', 'IsSuperuser']: # Проверяем наличие прав пользователя
            self.model.set_ingredients(new_ingredients) # Устанавливаем новые ингредиенты в модели return "Рецепт изменен!"  # Возвращаем сообщение об успешном изменении
            return "Рецепт изменен!"
        else:
            return "forbidden" # Возвращаем сообщение о запрете

    def set_price(self, user_rights, new_float_price): # Устанавливаем цену в зависимости от прав пользователя
        if user_rights in ['Admin', 'IsStaff', 'IsSuperuser']: # Проверяем наличие прав пользователя
            self.model.set_price(new_float_price)
            return "Цена изменена"  # Возвращаем сообщение об успешном изменении
        else:
            return "forbidden" # Возвращаем сообщение о запрете

    # Устанавливаем вес в зависимости от прав пользователя
    def set_weight(self, user_rights, new_weight_float):

        if user_rights in ['Admin', 'IsStaff', 'IsSuperuser']: # Проверяем наличие прав пользователя
            self.model.set_weight(new_weight_float) # Устанавливаем новый вес в модели
            return "Вес изменен" # Возвращаем сообщение об успешном изменении
        else:
            return "forbidden" # Возвращаем сообщение о запрете

    # Устанавливаем изображение в зависимости от прав пользователя
    def set_picture(self, user_rights, new_picture):
        if user_rights in ['Admin', 'IsStaff', 'IsSuperuser']: # Проверяем наличие прав пользователя
            self.model.set_picture(new_picture)
            return "Изображение изменено" # Возвращаем сообщение об успешном изменении
        else:
            return 'forbidden' # Возвращаем сообщение о запрете

    # Сохраняем заказ в JSON файл
    def save_order_to_json(self, order): # Получаем данные из JSON файла в зависимости от прав пользователя
        """Обеспечивает возможность сохранять модель."""
        return self.model.save_order_to_json(order)

    def get_data_from_json(self, user_rights, filename):
        """Пользователь предоставляет права и имя файла:
         Система проверяет доступ к файлу:
         Если доступ разрешён:
         система передаёт информацию о заказе.
         Если доступ запрещён:
         система выдаёт соответствующее сообщение."""
        if user_rights in ['Admin', 'IsStaff', 'IsSuperuser']:
            return self.model.get_data_from_json(filename)
        else:
            return 'forbidden' # Возвращаем сообщение о запрете