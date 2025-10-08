from random import random, randint, choice, shuffle
#import random as rd
import time
import json
import tkinter as tk
import psutil # Viktigt bibliotek för att kolla systemresurser!
import os

print(random())

dice_cast = randint(1, 6)
print(dice_cast)

names = ["Adam", "Bert", "Calle", "David", "Erik"]
random_name = choice(names)
print(random_name)

shuffle(names)

print(names)


for name in names:
    print("Getting name...")
    #time.sleep(2)
    print(f"Name: {name}")

x = 1.5
y = 3.0

my_tuple = (x, y)


# PSUTIL
#print(psutil.cpu_percent())


# JSON file reading/writing
def write_to_file():
    data = {"name": "Adam", "age": 21, "city": "Stockholm"}
    with open("data_file.json", "w") as write_file:
        json.dump(data, write_file)

def read_from_file():
    with open("data_file.json", "r") as read_file:
        data_loaded = json.load(read_file)
        print(data_loaded)
        print(type(data_loaded))

write_to_file()
read_from_file()

# TKINTER GUI

root = tk.Tk()
root.title("Exempel")

def hello():
    print("Hej från tkinter!")

btn = tk.Button(root, text="Klicka mig", command=hello)
btn.pack()

root.mainloop()


my_str = "410815"

print(my_str.isdigit()) # True if all characters in the string are digits
print(my_str.isalpha()) # True if all characters in the string are alphabetic
print(my_str.isnumeric()) # True if all characters in the string are numeric
