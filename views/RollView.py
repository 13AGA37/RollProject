class RollView:
    """Класс, который позволяет пользователю получать информацию и предоставлять данные."""

    def __init__(self, controller):
        """Конструктор, который запускается при создании экземпляра класса RollController."""
        self.controller = controller # Сохраняем экземпляр контроллера

    def print_restaurant_menu(self): # Печатаем меню ресторана, используя контроллер
        """Предоставляет данные, которые были получены от соответствующего устройства управления."""
        print(self.controller.get_restaurant_menu())

    # Печатаем меню сайта, используя контроллер

    def print_site_menu(self):
        """Сообщает данные, полученные от соответствующего управляющего устройства."""
        print(self.controller.get_site_menu())
        """Способы сбора информации от пользователя.
        В процессе сбора данных осуществляется проверка их типа. 
        Если данные соответствуют требованиям, они передаются на контроллер, который отвечает за их обработку. 
        В зависимости от ответа контроллера, пользователю выводится соответствующее сообщение:
        если ответ положительный, то пользователь получает уведомление;
        если ответ отрицательный, то пользователь получает сообщение «Нет доступа».
        В случае несоответствия данных требованиям, пользователю сообщается об ошибке."""
    # Устанавливаем ингредиенты в зависимости от прав пользовател
    def set_ingredients(self, user_rights, new_ingredients):
        if type(new_ingredients) is not list: # Проверяем тип входных данных
            print("Неверный тип данных!!!!")
            return
        set_ingredients_response = self.controller.set_ingredients(user_rights, new_ingredients)
        if set_ingredients_response == 'forbidden': # Проверяем наличие прав доступа
            print("Нет права доступа!")
        else:
            print(set_ingredients_response)

    def set_price(self, user_rights, new_price): # Устанавливаем цену в зависимости от прав пользователя
        try:
            new_float_price = float(new_price)
        except ValueError: # Пытаемся преобразовать цену в float except ValueError:
            print("Неверный тип данных!!!!")
            return
        set_price_response = self.controller.set_price(user_rights, new_float_price)
        if set_price_response == 'forbidden':
            print("Нет права доступа!") # Проверяем наличие прав доступа
        else:
            print(set_price_response)

    # Устанавливаем вес в зависимости от прав пользователя
    def set_weight(self, user_rights, new_weight):
        try:
            new_weight_float = float(new_weight)
        except ValueError:
            print("Неверный тип данных!!!!")
            return
        set_weight_response = self.controller.set_weight(user_rights, new_weight_float) # Пытаемся преобразовать вес в float
        if set_weight_response == 'forbidden': # Проверяем наличие прав доступа
            print("Нет права доступа!")
        else:
            print(set_weight_response)
    # Устанавливаем изображение в зависимости от прав пользователя
    def set_picture(self, user_rights, new_picture):
        set_picture_response = self.controller.set_picture(user_rights, new_picture)
        if set_picture_response == 'forbidden':# Проверяем наличие прав доступа
            print("Нет права доступа!")
        else:
            print(set_picture_response)
    # Сохраняем заказ в JSON файл
    def save_order_to_json(self, order):
        """Способ отображения данных о статусе заказа."""
        print(self.controller.save_order_to_json(order))
    # Получаем данные из JSON файла в зависимости от прав пользователя
    def get_data_from_json(self, user_rights, filename):
        """ Способ получения сведений о заказе из файла.
        Для работы метода необходимо указать права доступа и имя файла.
        Если права доступа корректны, метод возвращает данные о заказе.
        В случае некорректных прав доступа пользователь получает сообщение «Нет доступа!»."""
        get_data_from_json_response = self.controller.get_data_from_json(user_rights, filename)
        if get_data_from_json_response == 'forbidden':# Проверяем наличие прав доступа
            print("Нет права доступа!")
        else:
            print(get_data_from_json_response)