from typing import Any

import Abhishek


def greet_user():
    name = "Abhishek"
    print("Hello", name)
greet_user()

def hello():
    print("hello world")
hello()

def calculate_product(a,b):
    print(a*b)
calculate_product(3,4)

calculate_product(6,7)

# Barista order generator

def make_coffee(size,drink_type,customer_name):
    print("order_ready:","a" ,size,drink_type,"for",customer_name)
make_coffee("large","black coffee","Abhishek")

def equip_weapon(player_name,weapon_name,attack_power):
    print(f"weapon_ready:,{player_name} equipped {weapon_name} his {attack_power}")
equip_weapon("Abhishek","flame sword" ,str(50))

# The return statement
def diwali_bonus():
    return 5000
employee_salary = 10000 + diwali_bonus()
print(employee_salary)

def calculate_xp(base_xp,bonus_xp):
    return base_xp + bonus_xp
my_xp = calculate_xp(80,20)
needed_level_up = 160 - my_xp
print("Total xp earned by me:", my_xp)
print("the energy needed for level up is:",needed_level_up)

def level_up_stats(current_hp,current_mana):
    new_hp = current_hp + 20
    new_mana = current_mana + 5
    return new_hp, new_mana
my_hp, my_mana = level_up_stats(100, 60)
print("my new hp is:",my_hp)
print("my new mana is:", my_mana)

# the audio track booster
def boost_audio(volume,bass):
    new_volume = volume +  15
    new_bass = bass + 30
    return new_volume, new_bass
new_volume,new_bass = boost_audio(60,70)
print("my new volume is:",new_volume)
print("my new bass is:", new_bass)

# the challenege Audio limiting manager
Max_decibles = 85
def master_track(track_name, current_db , boost):
    new_db = current_db + boost
    if new_db > Max_decibles:
     new_db = Max_decibles

    headroom = Max_decibles - new_db
    return track_name, new_db, headroom
# the local variable

def my_func():
    my_var = 10
    print(my_var)
my_func()

# the resotion

def outer_fun():
    mes = "hello mommy how are you"
    res = "'" # to get res as the defined variable in outer_fun

    def inner_fun():
        nonlocal res# this is quite said to be as the modification of the global scope
        res = "good morning to all of you"
        print(mes)

    inner_fun()
    print(res)

outer_fun()

# the global scope

my_var = 100

def show_var():
    print(my_var)
    

  # my_var is now modified globally to 20

# the use case of the return function here we get the value none.

def calculate_sum(a,b):
    print(a+b)
my_sum = calculate_sum(10,20)
print(my_sum)

# the real use case of the return statement

def addition(a,b):
    return a+b
my_sum = addition(10,20)
print(my_sum)

#The another use case

def addition(a,b):
    return a+b
addition(10,20)
print(len([1,1,2,2,3]))


def pin_extractor(poem):
    secret_code = ''


poem = """Stars and the moon
shine in the sky
white and bright
until the end of the night"""

pin_extractor(poem)

