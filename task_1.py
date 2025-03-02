from abc import ABC, abstractmethod
import logging

logging.basicConfig(level=logging.INFO)


class Vehicle(ABC):
    def __init__(self, make: str, model: str) -> None:
        self.make: str = make
        self.model: str = model

    @abstractmethod
    def start_engine(self) -> None:
        pass


class Car(Vehicle):
    def start_engine(self) -> None:
        logging.info("%s %s : Двигун запущено", self.make, self.model)


class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        logging.info("%s %s  : Мотор заведено", self.make, self.model)


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Vehicle:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(f"{make} (US Spec)", model)

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(f"{make} (US Spec)", model)


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(f"{make} (EU Spec)", model)

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(f"{make} (EU Spec)", model)


# Використання
us_factory = USVehicleFactory()
eu_factory = EUVehicleFactory()
us_vehicle1 = us_factory.create_car("Toyota", "Corolla")
eu_vehicle1 = eu_factory.create_car("Toyota", "Corolla")
us_vehicle1.start_engine()
eu_vehicle1.start_engine()

us_vehicle2 = us_factory.create_motorcycle("Harley-Davidson", "Sportster")
eu_vehicle2 = eu_factory.create_motorcycle("Harley-Davidson", "Sportster")
us_vehicle2.start_engine()
eu_vehicle2.start_engine()
