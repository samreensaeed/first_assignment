#Exercise 3-4. Guest List
guest_list= ["Mehwish","Saira","Ayesha"]
for name in guest_list:
    print("Hey " + name + ", I would like to invite you for dinner at my place.\n")

#Exercise 3-5. Changing Guest List
del guest_list[1]
print(guest_list)

for name in guest_list:
    print("Hey " + name + ", I would like to invite you for dinner at my place.\n")

#Exercise 3-6. More Guests
print("Hey Guys! I found a bigger dinner table")
guest_list.insert(0,"Kinza")
guest_list.insert(2,"Fatima")
guest_list.append("Filza")
print(guest_list)
for name in guest_list:
    print("Hey " + name + ", I would like to invite you for dinner at my place.\n")

#Exercise 3-7. Shrinking Guest List
print("Sorry for some personal issues, i can invite only two people.")
print(guest_list)
cancel_invitation_1 = guest_list.pop()
print("Sorry " + cancel_invitation_1 + ", You're not invited.\n")
cancel_invitation_2 = guest_list.pop()
print("Sorry " + cancel_invitation_2 + ", You're not invited.\n ")
cancel_invitation_3 = guest_list.pop()
print("Sorry " + cancel_invitation_3 + ", You're not invited.\n ")
print(guest_list)
for name in guest_list:
    print("Hey " + name + ", I would like to invite you for dinner at my place.\n")
guest_list.remove("Kinza")
guest_list.remove("Mehwish")
print(guest_list)

#Exercise 3-8. Seeing the World
places = ["makkah","kashmir","swat","london","madina"]
print("Here is the original list:")
print(places)
print("\n Here is the sorted list:")
print(sorted(places))

places.reverse()
print(places)

places.reverse()
print(places)

places.sort()
print(places)

places.sort(reverse=True)
print(places)

#Exercise 3-9. Dinner Guests
print(len(guest_list))

#Exercise 3-10. Every Functions
cities = ["karachi","islamabad","gilgit","lahore","quetta"]
cities.sort()
print(cities)

cities.reverse()
print(cities)

cities.append("sukkur")
print(cities)

print(len(cities))

#Exercise 4-10. Slices
animals = ["Rabbit","Dog","Horse","Elephant","Cat","Lion","Camel"]
print(animals[0:3])  #First three items in the list

print(animals[2:5])  #Three items from the Middle

print(animals[4:7])  #Last three items in the list

#Exercise 4-11. My Pizzas, Your Pizzas
my_pizzas = ["fajita","chicken tikka","super supreme"]
friend_pizzas = my_pizzas[:]

my_pizzas.append("cheese max")
for pizza in my_pizzas:
    print("My favorite pizza is "+ pizza + "." "\n")

friend_pizzas.append("pepperoni")
for friend_pizza in friend_pizzas:
    print("My friend favorite pizza is " + friend_pizza + "." "\n")

#Exercise 4-12. More Loops
my_foods = ["pizza","falafel","corrot cake"]
friends_food = my_foods[:]

for food in my_foods:
    print("My favorite pizza is "+ food + "." "\n")

for friend_food in friends_food:
    print("My favorite pizza is "+ friend_food + "." "\n")

#Exercise 4-13. Buffet
buffet_foods = ("Biryani","Qorma","Haleem","Karahi","Nihari")
for buffet_food in buffet_foods:
    print(buffet_food)
#buffet_foods.append("Kabab")
print(buffet_foods)

print("Revised Menu" "\n")
buffet_foods = ("Biryani","Qorma","Haleem","Kabab","achar gosht")
for buffet_food in buffet_foods:
    print(buffet_food)


