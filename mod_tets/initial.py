from  dataclasses import dataclass
from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def go():
        pass

class Car(Vehicle):
    def go(self):
        print("car is going")
# vehicle = Vehicle()
bmw = Car()

bmw.go()


def hello_world():
    print("This is hello world from initial.py")

def name():
    print("This is name function from initial.py")