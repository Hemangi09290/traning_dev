import os

"use of inheritance"
"here in the class multilevel inheritance is explaned with accessing object from parent class from subclass"
class Animals:
    legs = "Animals has four legs" 
    print(legs)
class FarmAnimals(Animals):
    pass
class WildAnimals(FarmAnimals):
    pass
wildanimalsobj=WildAnimals()
wildanimalsobj.legs

"use of inheritance is explained with super function"
class Vehicle:
    def start(self):
        print("Starting engine")
    def stop(self):
        print("Stopping engine")                            
class TwoWheeler(Vehicle):
    def say(self):
        super().start()
        print("I have two wheels")
        super().stop()                            
jupiter=TwoWheeler()
jupiter.say()