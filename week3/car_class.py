class Car:

    # Car class represents a vehicle with basic attributes and actions.
    def __init__(self, brand, speed=0, license_plate=""):
        """
        Initialize a new Car instance.
        :param brand: The brand of the car (str)
        :param speed: The current speed of the car (int)
        :param license_plate: The car's license plate (str)
        """
        self.brand = brand
        self.speed = speed  # Current speed in km/h
        self.id = license_plate

    def __str__(self):
        return f"Brand: {self.brand}, Speed={self.speed}"

    def accelerate(self):
        self.speed += 10 # Syntaktiskt socker
        # self.speed = self.speed + 10
        return self.speed

    def brake(self):
        if (self.speed <= 0):
            return 0
        else:
            self.speed -= 10
            return self.speed
        
    def honk(self):
        print("Honk! Honk!")


def change_speed(car: Car, accelerate=True):
    if accelerate:
        return car.accelerate()
    else:
        return car.brake()


car1 = Car("Saab", 30, "XYZ987")
car2 = Car("Volvo", 20, "ABC123")
car3 = Car("Audi", 50, "XKA748")

car1.accelerate()
print(car1.speed)
car1.brake()
print(car1.speed)
car1.brake()

car_dict = {
    "XYZ987": car1,
    "ABC123": car2,
    "XKA748": car3
}

accelerate = input("Do you want to accelerate or brake? a/b ").lower()
chosen_car = input("For which car do you want to acc/brake? ").lower()
if accelerate == "a": # User wants to accelerate
    new_speed = change_speed(car_dict[chosen_car], True)
elif accelerate == "b": # User wants to brake
    new_speed = change_speed(car_dict[chosen_car] , False)
else:
    print("Invalid choice, please choose a/b")

print(f"New speed for {chosen_car} is {new_speed}")
