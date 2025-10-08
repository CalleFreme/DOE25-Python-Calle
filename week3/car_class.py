class Car:

    brake_amount = 10
    # Car class represents a vehicle with basic attributes and actions.
    def __init__(self, brand, speed=0, license_plate=""):
        """
        This is a docstring explaining the __init__ method.
        Initialize a new Car instance.
        :param brand: The brand of the car (str)
        :param speed: The current speed of the car (int)
        :param license_plate: The car's license plate (str)
        :return: None
        """
        self.brand = brand
        self.speed = speed  # Current speed in km/h
        self.id = license_plate

    def __str__(self):
        return f"Brand: {self.brand}, Speed={self.speed}, License Plate={self.id}"

    def accelerate(self):
        self.speed += 10 # Syntaktiskt socker
        # self.speed = self.speed + 10
        return self.speed

    def brake(self):
        '''
        Reduces the speed of the car by a fixed amount.
        :return: The new speed of the car (int)
        '''
        if (self.speed < Car.brake_amount):
            return self.speed
        else:
            self.speed -= Car.brake_amount
            return self.speed
        
    def honk(self):
        print("Honk! Honk!")

    def get_id(self):
        return self.id


def change_speed(car: Car, accelerate=True) ->  int:
    if accelerate:
        return car.accelerate()
    else:
        return car.brake()


car1 = Car("Saab", 30, "XYZ987")
car2 = Car("Volvo", 20, "ABC123")
car3 = Car("Audi", 50, "XKA748")
car4 = Car("Saab", 30, "XGA612")

car1.accelerate()
print(car1.speed)
car1.brake()
print(car1.speed)
car1.brake()

car_dict = {
    car1.get_id(): car1,
    car2.get_id(): car2,
    car3.get_id(): car3,
    "XGA612": car4 # Hårdkodad nyckel
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
