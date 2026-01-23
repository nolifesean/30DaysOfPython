# Day 6 30 Days of Python
# Exercises Level 1

empty_tuple = ()
sisters = ('Macy', 'Lara')
brothers = ('Levy', 'Angelo', 'Sean')

siblings = brothers + sisters
print("Siblings:", siblings)
print("Number of siblings:", len(siblings))

family_members = list(siblings)
family_members.append("Senen")
family_members.append("Liezl")
tuple(family_members)
print("Family members:", family_members)

# Exercises Level 2
print("\n==============================================")
bro1, bro2, bro3, sis1, sis2, *parents = family_members
print("Brother 1:", bro1)
print("Brother 2:", bro2)
print("Brother 3:", bro3)
print("Sister 1:", sis1)
print("Sister 2:", sis2)
print("Parents:", parents)
print("\n==============================================")

fruits = ("Apple", "Strawberry", "Orange", "Lemon")
vegetables = ("Celery", "Potato", "Lettuce", "Beans", "Tomato")
animal_products = ("Meat", "Cheese", "Milk", "Yogurt")

food_stuff_tp = fruits + vegetables + animal_products
food_stuff_lt = list(food_stuff_tp)
middle_item = food_stuff_tp[len(food_stuff_tp)//2:len(food_stuff_tp)//2+1]
print("Food stuff tuple:", food_stuff_tp)
print("Middle item:", middle_item)
first_three = food_stuff_lt[0:3]
last_three = food_stuff_lt[-3:]
print("First three items:", first_three)
print("Last three items:", last_three)

del food_stuff_tp

print("\n==============================================")
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Nordic Countries:", nordic_countries)
print("Is Estonia a nordic country?:", 'Estonia' in nordic_countries)
print("Is Iceland a nordic country?:", 'Iceland' in nordic_countries)