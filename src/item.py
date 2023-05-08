import csv

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
    def load_csv():
        data = []
        with open('src/items.csv', 'r', encoding='windows-1251') as csvfile:
            reader = csv.DictReader(csvfile)
            for item in reader:
                data.append(item)
            return data
        
    @classmethod
    def instantiate_from_csv(cls):
        data = cls.load_csv()
        for line in data:
            cls(
                line['name'],
                cls.string_to_number(line['price']),
                cls.string_to_number(line['quantity'])
            )
        
    @staticmethod
    def string_to_number(number_str):
        if "." in number_str:
            one = number_str.split(".")
            return int(one[0])
        return int(number_str)
        