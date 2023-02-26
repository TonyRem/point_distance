# импортируем функции из библиотеки math для рассчёта расстояния
from math import radians, sin, cos, acos


class Point:
    def __init__(self, latitude, longitude):
        self.latitude = radians(latitude)
        self.longitude = radians(longitude)

    # считаем расстояние между двумя точками в км
    def distance(self, other):
        cos_d = (sin(self.latitude) * sin(other.latitude) 
                + cos(self.latitude) * cos(other.latitude)
                * cos(self.longitude - other.longitude))

        return round(6371 * acos(cos_d), 3)


class City(Point):
    def __init__(self, latitude, longitude, name, population):
        # допишите код: сохраните свойства родителя
        # и добавьте свойства name и population
        super().__init__(latitude, longitude)
        self.name = name
        self.population = population

    def show(self):
        print(f"Город {self.name}, население {self.population} чел.")


class Mountain(Point):
    # допишите код: напишите конструктор, в нём сохраните свойства родителя
    # и добавьте свойства name и height
    def __init__(self, latitude, longitude, name, height):
        super().__init__(latitude, longitude)
        self.name = name
        self.height = height


    def show(self):
        print(f'Высота горы {self.name} - {self.height} м.')
    # Создайте метод show(self):
    # информацию о горе нужно вывести в формате:
    # "Высота горы <название> - <высота> м."


# эта функция печатает расстояние
# между двумя любыми наследниками класса Point
def print_how_far(geo_object_1, geo_object_2):
    print(f'От точки «{geo_object_1.name}» до '
          f'точки «{geo_object_2.name}» — '
          f'{geo_object_1.distance(geo_object_2)} км.')


# основной код
moscow = City(55.7522200, 37.6155600, 'Москва', 12615882)
everest = Mountain(27.98791, 86.92529, 'Эверест', 8848)
chelyabinsk = City(55.154, 61.4291, 'Челябинск', 1200703)
yerevan = City(40.1811, 44.5136, 'Ереван', 1093485)
ararat = Mountain(39,855403, 'Арарат', 5137)
bucharest = City(44.4323, 26.1063, 'Бухарест', 1877155)
dubai = City(25.0657, 55.1713, 'Дубай', 1137347)

moscow.show()
yerevan.show()
print_how_far(moscow, ararat)
print_how_far(moscow, yerevan)
print_how_far(ararat, yerevan)
print_how_far(bucharest, yerevan)
print_how_far(bucharest, moscow)
print_how_far(dubai, yerevan)
print_how_far(dubai, moscow)