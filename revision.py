# the revision of all the basics of python.


# the common data types in python.


my_string_var = "hello there"
print(my_string_var)
my_string_var_2 = "how are you miss"
print(my_string_var_2)

gratitude = f"Abhishek says to Harman {my_string_var} the beautiful lady {my_string_var_2}"
print(gratitude)
 # the combination of the boolean with conditionals .

# the challenge

is_affiliated_with_school = True
is_student = False
if not is_affiliated_with_school:
    print("Access denied:","not part of the school")
else:
    print("Welcome to the picnic!")
    if is_student:
        print("Here is your lunchbox")
    else:
        print("Here is your teacher lanyard")

# the lists

my_list = ["apple","banana","sandwich"]
my_list[0] = "grapes"
print(my_list)

fruit_salad = ["apple","banana","sandwich"]
fruit_salad.append("Mango")
print(fruit_salad)

# the inserting in lists
fruit_salad.insert(1,"blackberry")
print(fruit_salad)

# Adding multiple items at once (.extend())

fruit_salad.extend(["orange","mango"])
print(fruit_salad)

# Removing an item by its index (.pop())
fruit_salad.pop(2)
print(fruit_salad)

def outer_func():
    msg = 'Hello there!'
    print(msg)


def outer_func():
    msg = 'Hello there!'
    res = "'"
    def inner_func():
        nonlocal res
        res  = "how are yop"
        print(msg)

    inner_func()
    print(res)
outer_func()


example_list = ['example', 'dashed', 'name']

joined_str = ' '.join(example_list)
print(joined_str)  # ?

# the profile generator.
first_name = input()
birth_age = input()
favorite_hobby = input()
calculated_age = 2026-int(birth_age)
print("hello" + first_name+ "welcome to the mr Benjamin profile generator")
print(f"you are {calculated_age} years old and you love {favorite_hobby} ")
if calculated_age > 18:
    print("status:","Adult")
else:
    print("status:","Friend")
def pin_extractor(poem):
    secret_code = ''
    lines = poem.split('\n')
    for line_index, line in enumerate(lines):
        (line_index, line)
        words = line.split()
        (str(len(words[line_index])))
        secret_code += str(len(words[line_index]))
    return secret_code


poem = """Stars and the moon
shine in the sky
white and bright
until the end of the night"""

pin_extractor(poem)




