import random
from typing import Union


class Person:
    """Описывает игрового персонажа"""

    def __init__(self, name: str, max_health: int):
        """
        Создание игрового персонажа

        :param name: Имя персонажа
        :param max_health: Максимальное здоровье

        При создании персонажа его текущее здоровье автоматически устанавливается равным его максимальному здоровью
        """
        self.name = name
        self.max_health = max_health
        self._current_health = max_health  # Непубличный параметр, необходимо обрабатывать изменение параметра

    @property
    def name(self) -> str:
        """Геттер имени персонажа"""
        return self._name

    @name.setter
    def name(self, name):
        """
        Сеттер имени персонажа

        :param name: Имя персонажа
        """
        if not isinstance(name, str):
            raise TypeError("Имя персонажа должно быть строкой")
        self._name = name  # Непубличный параметр, необходимо проверить тип

    @property
    def max_health(self) -> int:
        """
        Геттер максимального здоровья персонажа

        :return: Максимальное здоровье персонажа
        """
        return self._max_health

    @max_health.setter
    def max_health(self, max_health):
        """
        Сеттер максимального здоровья персонажа

        :param max_health: Максимальное здоровье персонажа
        """
        if not type(max_health) == int:
            raise TypeError("Максимальное здоровье должно быть целым числом")
        if not max_health > 0:
            raise ValueError("Максимальное здоровье должно быть положительным числом")
        self._max_health = max_health  # Непубличный параметр, необходимо проверить тип и значение

    @property
    def current_health(self) -> int:
        """
        Геттер текущего здоровья персонажа

        :return: Текущее здоровье персонажа
        """
        return self._current_health

    def __str__(self) -> str:
        return f"{self.__class__.__name__} {self.name!r}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, max_health={self.max_health})"

    def taking_damage(self, damage: int) -> None:
        """
        Метод нанесения урона персонажу

        :param damage: Величина урона

        Если после нанесения урона здоровье персонажа становится равным 0 или отрицательным, персонаж умирает
        """
        self._current_health -= damage
        if self._current_health <= 0:
            self.kill()

    def kill(self):
        """Метода убийства персонажа"""
        # Описать способ удаления экземпляра
        print(f"{self.__class__.__name__} {self.name!r} is killed!")


class Warrior(Person):
    """Описывает воина"""

    def __init__(self, name: str, max_health: int, damage: int):
        """
        Создание воина

        :param name: Имя персонажа
        :param max_health: Максимальное здоровье
        :param damage: Урон персонажа
        """
        super().__init__(name, max_health)
        self.damage = damage

    def attack(self, person: Person) -> None:
        """
        Метода атаки воином другого персонажа

        :param person: Атакуемый персонаж
        """
        if not isinstance(person, Person):
            raise TypeError("Атакуемый персонаж должен быть экземпляром класса или подкласса Person")
        person.taking_damage(self.damage)  # Нанесение урона атакуемому персонажу
        print(f"{self.__class__.__name__} {self.name} наносит {person.__class__.__name__} {person.name}"
              f" урон {self.damage}")

    @property
    def damage(self) -> int:
        return self._damage

    @damage.setter
    def damage(self, damage: int) -> None:
        if not type(damage) == int:
            raise TypeError("Значение урона должно быть целым числом")
        if not damage > 0:
            raise ValueError("Значение урона должно быть положительным")
        self._damage = damage  # Непубличный параметр, необходимо проверить значение

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, max_health={self.max_health}, damage={self.damage})"
        # Магический метод переопределяется, поскольку для создания воина требуется больше параметров,
        # чем для создания экземпляра родительского класса


class Building:
    """Класс описывает возможные строения"""
    pass  # класс пока не реализован


class Builder(Person):
    """Описывает строителя"""

    def __init__(self, name: str, max_health):
        """
        Создание строителя

        :param name: Имя персонажа
        :param max_health: Максимальное здоровье
        """
        super().__init__(name, max_health)

    def build(self, building: str) -> Building:
        """
        Метод строительства сооружения

        :param building: Сооружаемое строение в виде строки
        :return: Возвращает строение
        """
        # Метод пока не реализован
        # Передаваемая строка проверяется на возможность построения данного сооружения


class Plant:
    """
    Класс описывает возможные растения для посадки фермером
    """
    pass  # класс пока не реализован


class Farmer(Person):
    """Описывает фермера"""

    def __init__(self, name: str, max_health):
        """
        Создание фермера

        :param name: Имя персонажа
        :param max_health: Максимальное здоровье
        """
        super().__init__(name, max_health)

    def sow(self, plant: Plant) -> Building:
        """
        Метод для посева фермером растения

        :param plant: Засеиваемое растение
        :return: возвращает плантацию в виде строения
        """
        # Метод пока не реализован


class Archer(Warrior):
    """Описывает лучника"""

    def __init__(self, name: str, max_health: int, damage: int, attack_range: Union[int, float]):
        """
        Создание лучника

        :param name: Имя персонажа
        :param max_health: Максимальное здоровье
        :param damage: Урон персонажа
        :param attack_range: Дальность атаки
        """
        super().__init__(name, max_health, damage)
        self.attack_range = attack_range

    def attack(self, person: Person) -> None:
        """
        Метода атаки лучником другого персонажа

        :param person: Атакуемый персонаж
        """
        # Используется перегрузка типа для добавления возможности промаха
        if not isinstance(person, Person):
            raise TypeError("Атакуемый персонаж должен быть экземпляром класса или подкласса Person")
        if random.random() > 0.2:
            person.taking_damage(self.damage)  # Нанесение урона атакуемому персонажу c вероятностью 80%
            print(f"{self.__class__.__name__} {self.name!r} попал в {person.__class__.__name__} {person.name}"
                  f" и нанёс урон {self.damage}")
        else:
            print(f"{self.__class__.__name__} {self.name!r} промахнулся")


    @property
    def attack_range(self) -> Union[int, float]:
        return self._attack_range

    @attack_range.setter
    def attack_range(self, attack_range: Union[int, float]) -> None:
        if not (type(attack_range) == int or type(attack_range) == float):
            raise TypeError("Значение дальности атаки должно быть целым числом или числом с плавающей точкой")
        if not attack_range > 0:
            raise ValueError("Значение дальности атаки должно быть положительным")
        self._attack_range = attack_range  # Непубличный параметр, необходимо проверить значение

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, max_health={self.max_health}, damage={self.damage}, " \
               f"attack_range={self.attack_range})"
    # Магический метод переопределяется, поскольку для создания лучника требуется больше параметров,
    # чем для создания экземпляра родительского класса


class Swordsman(Warrior):
    """Описывает мечника"""

    def __init__(self, name: str, max_health: int, damage: int):
        """
        Создание мечника

        :param name: Имя персонажа
        :param max_health: Максимальное здоровье
        :param damage: Урон персонажа
        """
        super().__init__(name, max_health, damage)


if __name__ == "__main__":
    # Write your solution here
    swordsman1 = Swordsman("Alex", 100, 20)
    swordsman2 = Swordsman("Peter", 100, 20)
    archer = Archer("Sonya", 100, 20, 10)

    print(swordsman1, swordsman1.current_health)
    print(swordsman2, swordsman2.current_health)
    print(archer, archer.current_health)

    swordsman2.attack(swordsman1)  # Peter атакует Alex
    print(swordsman1, swordsman1.current_health)
    print(swordsman2, swordsman2.current_health)
    print(archer, archer.current_health)

    archer.attack(swordsman2)   # Sonya атакует Peter
    print(swordsman1, swordsman1.current_health)
    print(swordsman2, swordsman2.current_health)
    print(archer, archer.current_health)

    swordsman1.taking_damage(100)  # Alex получает большой урон
    # Swordsman 'Alex' is killed!
