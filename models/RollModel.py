import json
from json import JSONDecodeError
import time


class RollModel:
    """Модель, которая позволяет оформлять заказы, охватывает как рестораны, так и онлайн-сервисы."""

    def __init__(self, name: str, ingredients: list, price: float, weight: float, picture,
                 client_ingredients: list = None):
        """Конструктор модели, который получает информацию о заказе, заполняет нужные поля и возвращает объект класса."""
        self.__name = name # Приватный атрибут для названия ролла
        self.__ingredients = ingredients # Приватный атрибут для ингредиентов
        self.__price = price  # Приватный атрибут для цены
        self.__weight = weight  # Приватный атрибут для веса
        self.__picture = picture # Приватный атрибут для изображения
        if client_ingredients is not None: # Ингредиенты клиента, если они предоставлены else:
            self.__client_ingredients = client_ingredients  # По умолчанию - пустой список
        else:
            self.__client_ingredients = []

        """Разработаны методы получения значений полей класса RollModel."""

    def get_name(self):
        return self.__name

    def get_ingredients(self):
        return self.__ingredients

    def get_price(self):
        return self.__price

    def get_weight(self):
        return self.__weight

    def get_picture(self):
        return self.__picture

    def get_client_ingredients(self):
        return self.__client_ingredients # Устанавливаем новые ингредиенты для ролла

    def set_ingredients(self, new_ingredients: list):
        """Функция, которая позволяет добавлять новые компоненты, предварительно удаляя из списка старые."""
        if type(new_ingredients) is list: # Проверяем тип входных данных
            self.__ingredients.clear() # Очищаем существующие ингредиенты
            self.__ingredients.extend(new_ingredients) # Добавляем новые ингредиенты else:
        else:
            return "Ошибка неверный тип данных"
        """Созданы методы установки значений для других свойств."""
    # Устанавливаем новую цену для ролла
    def set_price(self, new_price):
        self.__price = new_price

    # Устанавливаем новый вес для ролла
    def set_weight(self, new_weight):
        self.__weight = new_weight

    # Устанавливаем новое изображение для ролла
    def set_picture(self, new_picture):
        self.__picture = new_picture

    # Добавляем ингредиенты клиента к роллу
    def add_client_ingredients(self):
        """Способ включения дополнительных компонентов, предложенных заказчиком."""
        if self.__client_ingredients:
            self.__ingredients.extend(self.__client_ingredients)

    # Создаем ролл с модификациями клиента
    def make_Roll(self):
        """Алгоритм приготовления роллов:
        Вызывается метод get_client_ingredients().
        Вызывается метод get_price().
        Вызывается метод get_weight().Проверяется наличие дополнительных ингредиентов.
        Вызывается метод add_client_ingredients().
        Собирается заказ с учётом заданных параметров.
        Если ингредиентов нет:
        Собирается заказ с учётом параметров, переданных при инициализации.
        В результате возвращается заказанное блюдо."""
        client_ingredients = self.get_client_ingredients() # Получаем ингредиенты клиента
        all_ingredients = self.get_ingredients() # Получаем существующие ингредиенты
        price = self.get_price() # Получаем цену
        weight = self.get_weight()
        if client_ingredients: # Если есть ингредиенты клиента
            self.add_client_ingredients() # Добавляем их к роллу
            all_ingredients = self.get_ingredients() # Обновляем все ингредиенты
            price = price + len(client_ingredients) * 100  # Корректируем цену на основе ингредиентов клиента
            weight = weight + len(client_ingredients) * 50  # Корректируем вес на основе ингредиентов клиента
        ordered_Roll = {
            # Создаем словарь для заказанного ролла
            'name': self.get_name(),
            'ingredients': all_ingredients,
            'price': price,
            'weight': weight
        }
        return ordered_Roll # Возвращаем заказанный ролл

    def save_order_to_json(self, order):
        """Способ для записи данных о заказе в файл  с  расширением.json.
         В качестве входных данных используется название заказа.
         На основе этого названия и времени заказа формируется имя файла.
         Затем заказ записывается в файл.
         После выполнения операции возвращается сообщение о том, какой заказ и где был сохранён."""
        # Сохраняем заказ в JSON файл
        ordered_roll = self.make_Roll()  # Создаем заказанный ролл
        filename = fr'orders\{round(time.time(), 2)}_{order}.json'  # Создаем имя файла с временной меткой
        with open(filename, 'w', encoding='utf-8') as fp: # Открываем файл для записи
            json.dump(ordered_roll, fp, ensure_ascii=False, indent=2)  # Записываем заказанный ролл в JSON
        return f"Заказ {order} сохранен в файл {filename}" # Возвращаем сообщение о подтверждении # Получаем данные из JSON файла

    @staticmethod
    def get_data_from_json(filename):
        """ Способ получения данных из сохранённого файла. В качестве входных данных используется имя файла.
        Данные преобразуются в формат, который может быть использован в Python.
        Результатом работы метода являются преобразованные данные."""
        try:
            with open(fr"{filename}.json", 'r', encoding='utf-8') as fp: # Открываем файл для чтения
                python_data = json.load(fp) # Загружаем данные JSON
        except FileNotFoundError:
            return "Файл не найден!!!" # Обрабатываем ошибку, если файл не найден
        except JSONDecodeError:
            return "Данные повреждены!!!/Неверный формат файла!!!"  # Обрабатываем ошибку, если данные повреждены except Exception:
        except Exception:
            return "Что-то пошло не так!!!" # Обрабатываем любые другие исключения
        else:
            return python_data # Возвращаем загруженные данные