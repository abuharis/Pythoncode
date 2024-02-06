from  dataclasses import dataclass
from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def go():
        pass

class Car(Vehicle):
    def go(self):
        print("car is going")
vehicle = Vehicle()
bmw = Car()

bmw.go()
