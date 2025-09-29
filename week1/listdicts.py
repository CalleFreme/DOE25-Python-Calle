

name_list = ["Calle", "Bert", "Adam"]

first_name = name_list[0]

# Common list methods:
print(len(name_list))
print(name_list)
name_list.append("David")
name_list.remove("Bert")
print(name_list)
name_list.sort()

min_str = "Call"
min_str = min_str + "e"
print(min_str)

# More:
name_list.reverse()
print(name_list)
name_list.clear()
print(name_list)

print(first_name)

phone_name_dict = {"Calle": "123-456", "Bert": "234-567", "Adam": "345-678", "Calle": "987-654", "Calle": "555-555"}
name_phone_dict = {"123-456": "Calle", "234-567": "Bert", "345-678": "Adam", "987-654": "Calle", "555-555": "Calle"}

phone_number = phone_name_dict["Calle"]
person_name = name_phone_dict["345-678"]

#new_number = input("New number: ")
#new_person = input("New name: ")
#phone_name_dict[new_number] = new_person

number_to_look_up = input("What number do you want to look up? ")

if number_to_look_up in name_phone_dict.keys():
    print("Exists")
    wanted_name = name_phone_dict[number_to_look_up]
else:
    print("Could not be found")
