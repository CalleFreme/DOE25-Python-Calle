
app_is_running = True

while app_is_running == True:
    print("Menyval 1")
    print("Menyval 2")
    print("Menyval 3")
    print("Avsluta: 4")
    menu_choice = input("Vilken meny? ")

    if (menu_choice == "1"):
        print("Välkommen till meny 1")
    elif (menu_choice == "2"):
        print("Välkommen till meny 2")
    elif (menu_choice == "3"):
        print("Välkommen till meny 3")
    elif (menu_choice == "4"):
        print("Avslutar")
        app_is_running = False
    else:
        print("Okänt val, försök igen")


animal_list = ["Hund", "Katt", "Fisk", "Häst"]

for animal in animal_list:
    print(animal)
    if animal == "Hund":
        print("Woof!")
    else:
        print("djhaphda")

print()

for i in range(3):
    print("Hej")
    

for i in range(len(animal_list)):
    print(animal_list[i])

