import os
from models.RollModel import RollModel
from controllers.RollController import RollController
from views.RollView import RollView

if __name__ == "__main__":
    # Определяем путь к изображению ролла

    image_path = os.path.abspath('images/RollFiladelfia.jpg.')
    # Создаем экземпляр RollModel с деталями ролла
    my_model = RollModel(
        name='Филадельфия', # Название ролла
        ingredients=["рис", "нори", "лосось", "авокадо", "сыр филадельфия", "огурец"], # Ингредиенты ролла
        price=400,# Цена ролла
        weight=240, # Вес ролла
        picture=image_path, # Путь к изображению ролла
        client_ingredients=['+соевый соус', '+палочки', '+имбирь', '+вассаби' ] # Дополнительные ингредиенты от клиента
    )
    # Создаем контроллер для управления моделью ролла
    my_controller = RollController(my_model)
    # Создаем представление для взаимодействия с пользователем
    my_view = RollView(my_controller)
    # Печатаем меню ресторана и меню сайта
    my_view.print_restaurant_menu()
    my_view.print_site_menu()
    my_view.save_order_to_json(("филадельфия"))

    # Получаем данные из JSON файла для определенного заказа
    print()
    # Устанавливаем ингредиенты для пользователя и администратора
    my_view.get_data_from_json('Admin', r'orders\1728397109.96_Филадельфия_Стандарт_Стандарт')
    print()
    my_view.set_ingredients('user', ["рис", "нори", "лосось", "авокадо", "сыр филадельфия", "огурец"])
    my_view.set_ingredients('Admin', ("рис", "нори", "лосось", "авокадо", "сыр филадельфия", "огурец"))
    my_view.set_ingredients('Admin', ["рис", "нори", "лосось", "авокадо", "сыр филадельфия", "огурец"])
    print()
    # Устанавливаем цену для пользователя и администратора
    my_view.set_price('user', "400")
    my_view.set_price('Admin', "четыреста")
    my_view.set_price('Admin', "400")
    print()
    # Устанавливаем вес для пользователя и администратора
    my_view.set_weight('user', "250")
    my_view.set_weight('Admin', "двести пятьдесят")
    my_view.set_weight('Admin', "250")
    print()
    my_view.print_restaurant_menu()