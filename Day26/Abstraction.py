"""
hide the unneccessary information( Implememtion )

Abstract:
  1. Abstract Classes
  2. Abstract Methods ( Non Abstract Methods )

Abstract Classes and Methods are not supported by Python unlike Java but
Module can use the bring the concepts to our program


from abc import ABC, abstractmethod
WHERE abc is Package and ABC is Abstract Class, abstractmethods is Abstract Method


***abstarctmethod should implement in the subclass ( Concreate class)
"""

from abc import ABC, abstractmethod # this important because abstraction is not supported by Python but we can import the same
class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass


    def stop(self):
        print("Vehicle stopped")  #Vehicle stopped

    @abstractmethod
    def horn(self):
        pass

class car(vehicle):
  #start, horn are abstract method in abtract class, these must be implemented in concreate ( subclass)
    def start(self):
        print("Main Starting")  #Main Starting

    def horn(self):
        print("horn") #horn


c=car()
c.start()
c.stop()
c.horn()

