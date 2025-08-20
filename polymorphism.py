# Assignment 1: Designing my Own Class

class Car:
    def __init__(self, brand, model, fuel, speed=0):
        self.brand = brand
        self.model = model
        self.fuel = fuel
        self.speed = speed

    def accelerate(self, increase):
        if self.fuel > 0:
            self.speed += increase
            self.fuel -= increase * 0.2 
            return f"{self.brand} {self.model} accelerated to {self.speed} km/h. Fuel left: {self.fuel:.1f}L"
        else:
            return f"{self.brand} {self.model} has no fuel left!"

    def refuel(self, liters):
        self.fuel += liters
        return f"{self.brand} {self.model} refueled. Current fuel: {self.fuel:.1f}L"

    def __str__(self):
        return f"{self.brand} {self.model} | Speed: {self.speed} km/h | Fuel: {self.fuel:.1f}L"


# Inheritance Example
class SportsCar(Car):
    def __init__(self, brand, model, fuel, speed=0, turbo=False):
        super().__init__(brand, model, fuel, speed)
        self.turbo = turbo

    def accelerate(self, increase):
        if self.fuel > 0:
            boost = increase * 2 if self.turbo else increase
            self.speed += boost
            self.fuel -= boost * 0.3
            return f"{self.brand} {self.model} blasted to {self.speed} km/h (Turbo: {self.turbo}). Fuel left: {self.fuel:.1f}L"
        else:
            return f"{self.brand} {self.model} is out of fuel!"

    def __str__(self):
        return super().__str__() + f" | Turbo: {self.turbo}"


# Activity 2: Polymorphism Challenge! 
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclass must implement abstract method")

class CarVehicle(Vehicle):
    def move(self):
        return "Driving"

class Plane(Vehicle):
    def move(self):
        return "Flying"

class Boat(Vehicle):
    def move(self):
        return "Sailing"

class Bicycle(Vehicle):
    def move(self):
        return "Pedaling"


# My Test Example
if __name__ == "__main__":

    my_car = Car("Toyota", "Corolla", fuel=20)
    my_sportscar = SportsCar("Ferrari", "488 Pista", fuel=50, turbo=True)

    print(my_car)
    print(my_car.accelerate(30))
    print(my_car.refuel(10))

    print(my_sportscar)
    print(my_sportscar.accelerate(40))

    print("\n--- Polymorphism Challenge ---")
    vehicles = [CarVehicle(), Plane(), Boat(), Bicycle()]
    for v in vehicles:
        print(v.move())
