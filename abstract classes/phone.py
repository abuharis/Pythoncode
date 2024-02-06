from abc import ABC, abstractmethod

"""The abstract methods are declarable but not implementable. The child class must have these methods to create an object.
This is useful to create a template of a product. Without these features, the product cannot be created.
This avoids the mistakes of releasing a feature without a certain feature."""

class Phone(ABC):

    def __init__(self, brand: str) -> None:
        super().__init__()
        self.brand = brand

    @abstractmethod
    def power(self):
        return "50% battery remaining"
    
    @abstractmethod
    def switchoff(self):
        return "Switching off the phone"
    
    @abstractmethod
    def find_my_phone(self):
        pass


class Iphone(Phone):
    def __init__(self, brand: str) -> None:
        super().__init__(brand)

    def power(self):
        return "Battery is full"
    
    def switchoff(self):
        print("Switching off the phone") 
    
    def find_my_phone(self):
        raise NotImplementedError('The feature is not yet ready')

iphone = Iphone("12pro")
iphone.switchoff()
iphone.find_my_phone()
iphone.power()