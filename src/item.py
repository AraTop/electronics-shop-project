import csv
import os

class EmptyException(Exception):
    pass

class errorInstantiate(Exception):
    pass

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

        self.all.append(self)
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        return f"{self.name}"
    
    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        total_money = self.price * self.quantity
        return total_money

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            raise Exception(f"Длина наименования товара {name} превышает 10 симвовов")
        else:
            self.__name: str = name

    @staticmethod

    def load_csv(filename) -> list:
        """
        Получает данные из csv-файла
        :return: Список словарей из строк csv-файла
        """
        data = []
        filedir = os.path.dirname(os.path.abspath(__file__))
        try:
            with open(os.path.join(f'{filedir}', filename), 'r', encoding='windows-1251') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for item in csv_reader:
                    data.append(item)
                return data
        except:
            raise FileNotFoundError(f"Отсутствует файл {filename}")

    @classmethod
    def instantiate_from_csv(cls) -> None:
        """
        Инициализирует экземпляры класса Item данными из файла src/items.csv
        :return: None
        """

        filename = 'items.csv'
        cls.all = []
        data = cls.load_csv(filename)
        for line in data:
            try:
                cls(
                    line['name'],
                    cls.string_to_number(line['price']),
                    cls.string_to_number(line['quantity'])
                )
            except:
                raise InstantiateCSVError(f"Файл {filename} поврежден")
            
    @staticmethod
    def string_to_number(number_str):
        if "." in number_str:
            one = number_str.split(".")
            return int(one[0])
        return int(number_str)
        