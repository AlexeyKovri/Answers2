# TODO Написать 3 класса с документацией и аннотацией типов
from typing import Union
import doctest


class Car:
    """
    Документация на класс.
    Класс описывает модель автомобиля.
    """

    def __init__(self, max_speed: Union[int, float], color: str) -> None:
        """
        Инициализация экземпляра класса

        :param max_speed: Максимальная скорость автомобиля
        :param color: Цвет автомобиля

        Примеры:
        >>> car = Car(200, "Red")
        """
        self.max_speed = None
        self.set_max_speed(max_speed)
        self.color = None
        self.paint(color)

    def set_max_speed(self, max_speed: Union[int, float]) -> None:
        """
        Метод позволяет установить максимальную скорость автомобиля.

        :param max_speed: Максимальная скорость автомобиля

        :raise TypeError: Если максимальная скорость не является числом
        :raise ValueError: Если максимальная скорость не положительное число
        """
        if not isinstance(max_speed, (int, float)):
            raise TypeError("Максимальная скорость автомобиля должна иметь тип int или float")
        if not max_speed > 0:
            raise ValueError("Максимальная скорость автомобиля должна быть положительным числом")
        self.max_speed = max_speed

    def paint(self, color: str) -> None:
        """
        Метод позволяет покрасить автомобиль.

        :param color: Цвет автомобиля

        :raise TypeError: Если цвет автомобиля не является строкой
        """
        if not isinstance(color, str):
            raise TypeError("Цвет автомобиля должен быть строкой")
        self.color = color

    def get_color(self) -> str:
        """
        Метод возвращает цвет автомобиля.

        :return: Цвет автомобиля
        Пример:
        >>> car = Car(200, "Red")
        >>> car.get_color()
        'Red'
        """
        return self.color


class House:
    """
    Документация на класс.

    Класс описывает модель жилого дома
    """

    def __init__(self, floors_number: int, entrances_number: int, apartments_number: int):
        """
        Создание объекта дом
        :param floors_number: Количество этажей
        :param entrances_number: Количество подъездов
        :param apartments_number: Количество квартир

        Пример:
        >>> house = House(4, 5, 50)
        >>> house.get_condition()
        100.0

        """
        self.floors_number = floors_number
        self.entrances_number = entrances_number
        self.apartments_number = apartments_number
        self.residents_number = 0
        self.condition = 100.0

    def move_persons_into_apartment(self, persons_number: int) -> None:
        """
        Метод позволяет заселить людей в дом

        :param persons_number: Количество заселяемых людей
        """
        self.residents_number += persons_number

    def evict_persons(self, persons_number: int) -> None:
        """
        Метод позволяет выселить людей из дома

        :param persons_number: Количество выселяемых людей

        :raise ValueError: При попытке выселить больше людей, чем заселено
        """
        if persons_number > self.residents_number:
            raise ValueError("Не может быть выселено больше людей, чем заселено")
        self.residents_number -= persons_number

    def worsen_condition(self, damage_degree: float) -> None:
        """
        Метод ухудшает состояние дома.
        Скорость и степень ухудшения состояния самостоятельно определяется пользователем класса.

        :param damage_degree: Степень тяжести
        """
        self.condition -= damage_degree
        if self.condition < 0:
            self.destroy()

    def destroy(self) -> None:
        """
        Метод разрушает дом.
        """
        del self

    def get_condition(self) -> float:
        """
        Метод позволяет считать состояние дома

        :return: Состояние дома
        """
        return self.condition


class Builder:
    """
    Документация на класс.
    Класс описывает строителя.
    Строитель может возводить и ремонтировать дома.
    >>> builder = Builder("Alex", 30)
    >>> built_house = builder.build(4, 5, 50)
    >>> built_house.get_condition()
    100.0
    >>> built_house.worsen_condition(10)
    >>> built_house.get_condition()
    90.0
    >>> builder.repair(built_house, 5)
    >>> built_house.get_condition()
    95.0
    """

    def __init__(self, name: str, age: int):
        """
        Создание объекта строитель

        :param name: Имя строителя
        :param age: Возраст строителя
        """
        self.name = name
        self.age = age


    def build(self, floors_number: int, entrances_number: int, apartments_number: int) -> House:
        """
        Метод для построения жилого дома строителем

        :param floors_number: Количество этажей дома
        :param entrances_number: Количество подъездов дома
        :param apartments_number: Количество квартир дома
        :return: Дом с заданными параметрами
        """
        house = House(floors_number, entrances_number, apartments_number)
        return house

    def repair(self, house: House, repair_scope) -> None:
        """
        Метод для ремонта жилого дома строителем

        :param house: ремонтируемый дом
        :param repair_scope: Глубина ремонта
        """
        house.condition += repair_scope


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()

    pass
