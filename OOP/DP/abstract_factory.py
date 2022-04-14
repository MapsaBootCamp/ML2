from abc import ABC, abstractmethod


class AbstractFactory(ABC):

    @abstractmethod
    def create_product_chair(self) -> "AbstractChair":
        pass

    @abstractmethod
    def create_product_sofa(self) -> "AbstractSofa":
        pass


class ArtDeco(AbstractFactory):

    def create_product_chair(self):
        return ArtChair()
    
    def create_product_sofa(self):
        return ArtSofa()


class Victorian(AbstractFactory):

    def create_product_chair(self):
        return VictorianChair()
    
    def create_product_sofa(self):
        return VictorianSofa()


class Modern(AbstractFactory):
    def create_product_chair(self):
        return ModernChair()
    
    def create_product_sofa(self):
        return ModernSofa()


class AbstractChair(ABC):
    
    @abstractmethod
    def sit_(self):
        pass

class AbstractSofa(ABC):
    
    @abstractmethod
    def lamidan_(self):
        pass


class ArtChair(AbstractChair):

    def sit_(self):
        print("nashastan bar sandali honari")


class VictorianChair(AbstractChair):

    def sit_(self):
        print("nashastan bar sandali saltanati")


class ArtSofa(AbstractSofa):

    def lamidan_(self):
        print("lamidan bar kanape honari")


class VictorianSofa(AbstractSofa):

    def lamidan_(self):
        print("lamidan bar kanape saltanati")

class ModernChair(AbstractChair):

    def sit_(self):
        print("neshastan bar sandali modern")


class ModernSofa(AbstractSofa):

    def lamidan_(self):
        print("lamidan bar kanape modern")


def client_code(factory: AbstractFactory) -> None:

    product_a = factory.create_product_chair()
    product_b = factory.create_product_sofa()

    product_a.sit_()
    product_b.lamidan_()


if __name__ == "__main__":
    print("ye mahsul honari")
    client_code(ArtDeco())

    print("sakht mahsulat saltanat talabale taghutane")
    client_code(Victorian())

    client_code(Modern())
