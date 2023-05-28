from abc import ABC , abstractclassmethod, abstractmethod

# Interface for Chair, Sofa , Coffee Table

class Chair(ABC):
    CUSHION = ('SOFT','MEDIUM','HARD')

    @abstractmethod
    def hasLegs(self):
        pass

    @abstractmethod
    def sitOn(self):
        pass

class Sofa(ABC):
    CUSHION = ('SOFT','MEDIUM','HARD')

    @abstractmethod
    def hasLegs(self):
        pass

    @abstractmethod
    def sitOn(self):
        pass

class CoffeeTable(ABC):
    CUSHION = ('SOFT','MEDIUM','HARD')

    @abstractmethod
    def hasLegs(self):
        pass

    @abstractmethod
    def sitOn(self):
        pass


# End Products

class VictorianSofa(Sofa):
    def hasLegs(self):
        return (True,4)
    def sitOn(self):
        return self.CUSHION[0]
    
class ModernSofa(Sofa):
    def hasLegs(self):
        return super().hasLegs()
    def sitOn(self):
        return self.CUSHION[2]

class ArtDecoSofa(Sofa):
    def hasLegs(self):
        return super().hasLegs()
    def sitOn(self):
        return self.CUSHION[1]




class VictorianCoffeeTable(CoffeeTable):
    def hasLegs(self):
        return (True,4)
    def sitOn(self):
        return self.CUSHION[0]
    
class ModernCoffeeTable(CoffeeTable):
    def hasLegs(self):
        return super().hasLegs()
    def sitOn(self):
        return self.CUSHION[2]

class ArtDecoCoffeeTable(CoffeeTable):
    def hasLegs(self):
        return super().hasLegs()
    def sitOn(self):
        return self.CUSHION[1]



class VictorianChair(Chair):
    def hasLegs(self):
        return (True,4)
    def sitOn(self):
        return self.CUSHION[0]
    
class ModernChair(Chair):
    def hasLegs(self):
        return super().hasLegs()
    def sitOn(self):
        return self.CUSHION[2]

class ArtDecoChair(Chair):
    def hasLegs(self):
        return super().hasLegs()
    def sitOn(self):
        return self.CUSHION[1]
    



# Interface For Factory

class FurnitureFactory(ABC):
    @abstractmethod
    def createChair(self):
        pass

    @abstractmethod
    def createSofa(self):
        pass

    @abstractmethod
    def createCoffeeTable(self):
        pass


class ModernFurnitureFactory(FurnitureFactory):
    def createChair(self):
        return ModernChair()
    def createCoffeeTable(self):
        return ModernCoffeeTable()
    def createSofa(self):
        return ModernSofa()


class VictorianFurnitureFactory(FurnitureFactory):
    def createChair(self):
        return VictorianChair()
    def createCoffeeTable(self):
        return VictorianCoffeeTable()
    def createSofa(self):
        return VictorianSofa()

class ArtDecoFurnitureFactory(FurnitureFactory):
    def createChair(self):
        return ArtDecoChair()
    def createCoffeeTable(self):
        return ArtDecoCoffeeTable()
    def createSofa(self):
        return ArtDecoSofa()
