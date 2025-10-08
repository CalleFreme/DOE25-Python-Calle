

from car_class import Car

# ParkingHouse class manages a collection of parked cars.
class ParkingHouse:
    def __init__(self, capacity):
        """
        Initialize a new ParkingHouse instance.
        :param capacity: Maximum number of cars (int)
        """
        self.capacity = capacity
        self.cars = {}  # Dictionary to store parked cars by license plate

    def park_car(self, car: Car):
        """
        Park a car in the parking house if space is available.
        :param car: Car object to park
        """
        if len(self.cars) < self.capacity:
            if car.id in self.cars:
                print(f"Car with license plate {car.id} is already parked.")
            else:
                self.cars[car.id] = car
                print(f"Car with license plate {car.id} parked.")
        else:
            print("Parking house is full!")

    def remove_car(self, license_plate):
        """
        Remove a car from the parking house by license plate.
        :param license_plate: License plate of the car to remove (str)
        """
        if license_plate in self.cars:
            del self.cars[license_plate]
            print(f"Car with license plate {license_plate} removed.")
        else:
            print(f"No car with license plate {license_plate} found.")

    def list_cars(self):
        """
        List all cars currently parked.
        """
        if not self.cars:
            print("No cars parked.")
        else:
            for car in self.cars.values():
                print(car)