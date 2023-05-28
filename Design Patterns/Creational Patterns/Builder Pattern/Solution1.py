from __future__ import annotations
from abc import ABC, abstractmethod


class Vehical():
    "The Product"
    def __init__(self,wheals=0,engine=0,seats=0):
        self.wheals = wheals
        self.engine = engine
        self.seats = seats

class Car(Vehical):
    def __init__(self, wheals=0, engine=0, seats=0):
        super().__init__(wheals, engine, seats)
class Bike(Vehical):
    def __init__(self, wheals=0, engine=0, seats=0):
        super().__init__(wheals, engine, seats)


class IBuilder(ABC):
    @abstractmethod
    def reset(self) -> IBuilder:
        raise NotImplementedError
    @abstractmethod
    def setWheels(self,number:int) -> IBuilder:
        raise NotImplementedError

    @abstractmethod
    def setEngine(self,type:str) -> IBuilder:
        raise NotImplementedError

    @abstractmethod
    def setSeats(self,seats:int) -> IBuilder:
        raise NotImplementedError
    
    @abstractmethod
    def getResult(self):
        raise NotImplementedError
    

class CarBuilder(IBuilder):
    def __init__(self):
        self.car = Car()
    
    def reset(self) -> CarBuilder:
        self.car = Car()
        return self
    
    def setWheels(self, number: int) -> CarBuilder:
        self.car.wheels = number
        return self
    
    def setEngine(self, type: str) -> CarBuilder:
        self.car.engine = type
        return self
    
    def setSeats(self, seats: int) -> CarBuilder:
        self.car.seats = seats
        return self
    
    def getResult(self):
        return self.car
    
CarBuilder().setWheels().setSeats()


class BikeBuilder(IBuilder):
    def __init__(self):
        self.bike = Bike()
    
    def reset(self) -> BikeBuilder:
        self.bike = Bike()
        return self
    
    def setWheels(self, number: int) -> BikeBuilder:
        self.bike.wheels = number
        return self
    
    def setEngine(self, type: str) -> BikeBuilder:
        self.bike.engine = type
        return self
    
    def setSeats(self, seats: int) -> BikeBuilder:
        self.bike.seats = seats
        return self


class Director:
    """
    The Director Interface, creating the complex object
    """
    @abstractmethod
    @staticmethod
    def construct():
        raise NotImplementedError
    
class CarDirector:
    def construct():
        return Builder().setsetae(4).setEnigeg

class BikeDirectoe