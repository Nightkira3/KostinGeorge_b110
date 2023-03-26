__author__ = 'Костин Георгий'

"""Разработать модель предметной области в соответствии с вариантом:
Предметная область – автосалон. Разработать класс CarDealership, описывающий работу автосалона. Разработать класс Car, 
автомобиль описывается следующими параметрами: уникальный идентификатор, марка автомобиля, страна-производитель, 
год выпуска, объем двигателя, стоимость. Разработать класс Lorry на базе класс Car, 
грузовик характеризуется: весовым ограничение перевозки.
"""


class Car:
    def __init__(self, id, brand, country, year, engine_volume, price):
        """
        Конструктор класса Car
        id: уникальный идентификатор
        brand: марка автомобиля
        country: страна-производитель
        year: год выпуска
        engine_volume: объем двигателя
        price: стоимость
        """
        self.id = id
        self.brand = brand
        self.country = country
        self.year = year
        self.engine_volume = engine_volume
        self.price = price


class Lorry(Car):
    def __init__(self, id, brand, country, year, engine_volume, price, weight_limit):
        """
        Конструктор класса Lorry
        id: уникальный идентификатор
        brand: марка автомобиля
        country: страна-производитель
        year: год выпуска
        engine_volume: объем двигателя
        price: стоимость
        weight_limit: весовое ограничение
        """
        super().__init__(id, brand, country, year, engine_volume, price)
        self.weight_limit = weight_limit


class CarDealership:
    def __init__(self, name, location):
        """
        Конструктор класса CarDealership
        name: наименование автосалона
        location: местоположение автосалона
        """
        self.name = name
        self.location = location
        self.cars = []

    def add_car(self, car):
        """
        Добавление автомобиля в список
        car: экземпляр класса Car
        """
        self.cars.append(car)

    def list_cars(self):
        """
        Возвращает список автомобилей в наличии
        """
        return self.cars

    def find_car(self, id):
        """
        Поиск автомобиля по уникальному идентификатору
        """
        for car in self.cars:
            if car.id == id:
                return car
        return None

    def sell_car(self, id):
        """
        Продажа автомобиля по уникальному идентификатору
        """
        car = self.find_car(id)
        if car:
            self.cars.remove(car)
            return car
        else:
            return None
