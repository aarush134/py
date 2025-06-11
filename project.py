class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):
        print(f"The {self.color} {self.brand} is now driving!")

my_car = Car("Toyota", "red")
my_car.drive()
