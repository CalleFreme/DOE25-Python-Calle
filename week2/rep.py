
# Variabler

my_int = 15
#my_num_str = "15"
my_float = 15.0
my_bool = True
my_input_num_str = input("Skriv in ett värde 1-20")

if my_input_num_str.isdigit():
    if 1 <= int(my_input_num_str) <= 20:      
        my_sum = my_int + int(my_input_num_str)
        print(my_sum)
    else:
        print("Rätt datatyp, men värdet inte mellan 1-20.")
else:
    print("Given input är inte en siffra.")

my_product = my_int * my_input_num_str
print(my_product)
print()
# Printa

# Loopar

# while-loopar

counter = 0
user_name = input("Your name: ")
run_loop = True
while run_loop:
    counter += 1
    print(f"Hi, {user_name}, counter value: {counter}")
    #counter = counter + 1
    if counter > 10:
        run_loop = False

# break
counter = 0
while True:
    counter += 1
    print(f"Hi, {user_name}, counter value: {counter}")
    #counter = counter + 1
    if counter > 10:
        break

name_list = ["CAlle", "Bert", "Anna", "Adam", "Erik"]
            #  0         1      2        3      4
counter2 = 0
repetitions = int(input("How many repetitions"))
while counter2 < repetitions:
    print(name_list[counter2])
    print(f"Hi, {user_name}, counter value: {counter2 + 1}")
    #counter = counter + 1
    counter2 += 1
print("Loop over")

# Listor

person1 = "Calle"
person2 = "Adam"
person3 = "Anna"
#user_list = [person1, person2, person3]
#               0       1         2
user_list = ["Calle", "Calle", "Anna"]



print(user_list)
print(user_list[1])

# for-loopar

for user in user_list:
    print(user)

x = input("How many repetitions: ")
# range = [0, 1, 2, 3, 4]
for i in range(int(x)):
    for j in range(3):
        print(f"Print count for {i}, #{j+1}")

# Nested lists    
user_info1 = ["Calle", "9402108"]
user_info1.append("Boxvägen 5")
user_info2 = ["Adam", "850101", "Storgatan 5"]
user_info3 = ["Anna", "990505", "Lillvägen 3"]

user_data = [user_info1, user_info2, user_info3]

for user in user_data:
    for user_info in user:
        # Print each user's data on one line
        print(user_info, end=" | ")
    print()

while True:
    add_new_user = input("Do you want add a new user? Y/N ") # YES, Yes, yES, yes
    if add_new_user.upper() == "Y" or add_new_user.lower() == "yes":
        new_user_name = input("New name: ")
        new_personnr = input("New personnummer: ")
        new_adress = input("New adress: ")
        new_user = [new_user_name, new_personnr, new_adress]
        user_data.append(new_user)
    elif add_new_user.upper() == "N" or add_new_user.lower() == "no":
        break
    else:
        print("Choice not valid")

print("Min sträng")
print(user_data)

