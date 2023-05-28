from abc import ABC , abstractmethod

# Interface for Transport

class Transport(ABC):
    ROUTE = ('LAND','WATER','AIR')

    @abstractmethod
    def route():
        pass

    @abstractmethod
    def deliver():
        pass


# Interface For Logistics
class Logistics(ABC):
    @abstractmethod
    def createTransport():
        pass

    @abstractmethod
    def planDelivery():
        pass


# End Products
class Truck(Transport):
    def route(self):
        return self.ROUTE[0]
    
    def deliver():
        return 'Boxes'

class Ship(Transport):
    def route(self):
        return self.ROUTE[1]
    def deliver():
        return 'Containers'
    

class RoadLogistics(Logistics):
    def createTransport():
        return Truck()
    
    def planDelivery():
        pass

class SeaLogistics(Logistics):
    def createTransport():
        return Ship()
    def planDelivery():
        pass