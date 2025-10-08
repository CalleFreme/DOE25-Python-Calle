
# Sensor class represents a sensor with a name and tracks total count.
class Sensor:
    count = 0  # Class variable to track number of sensors

    def __init__(self, name):
        """
        Initialize a new Sensor instance.
        :param name: Name of the sensor (str)
        """
        self.name = name
        Sensor.count += 1
        print(f"Sensor count={Sensor.count}")

    def __str__(self):
        """
        Return a string representation of the sensor.
        """
        return f"Sensor: {self.name}, number of sensors: #{Sensor.count}"

# Example usage
s1 = Sensor("CPU")
s2 = Sensor("Temp")

print(s1)
print(s2)