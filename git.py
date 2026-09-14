# servers = [
#     {"name": "Server Alpha", "resolution": 720, "status": "Online"},
#     {"name": "Server Beta", "resolution": 1080, "status": "Offline"},
#     {"name": "Server Gamma", "resolution": 1080, "status": "Online"}
# ]
# this is our data we have to work on this data hn
""" hai here first of all we have to go with the for loop
  then we have to apply the conditionals in that for loop for   the different conditions lets first of all how we have togo with
  the for loop here for users in servers
  then the conditional if user """
def find_best_server(server_list):
    for server in server_list:
        if server["resolution"] == 1080 and server["status"]== "online":
             return server["name"]
    return "no 1080p servers available"
servers = [
    {"name": "Server Alpha", "resolution": 720, "status": "Online"},
    {"name": "Server Beta", "resolution": 1080, "status": "Offline"},
    {"name": "Server Gamma", "resolution": 1080, "status": "Online"}
]
# the vision dataset filter

# Your raw dataset
scraped_images = [
    {"file": "train_01.jpg", "format": "jpg", "width": 1024, "height": 1024, "corrupted": False},
    {"file": "train_02.png", "format": "png", "width": 256, "height": 256, "corrupted": False},  # Fails: too small
    {"file": "train_03.jpg", "format": "jpg", "width": 800, "height": 600, "corrupted": True},  # Fails: corrupted
    {"file": "train_04.webp", "format": "webp", "width": 1920, "height": 1080, "corrupted": False},
    # Fails: wrong format
    {"file": "train_05.png", "format": "png", "width": 800, "height": 800, "corrupted": False}
]

def filter_data(images):
    file_name = []
    for image in images:
        if image["format"] in ["jpg", "png"] and image["corrupted"] == False and image["width"] > 500 and image[
            "height"] > 500:
            file_name.append(image["file"])
    return file_name
print(filter_data(scraped_images))

# our third project
available_models = [
    {"name": "Qwen2.5-1.5B", "parameters": 1.5, "quantized": True, "ram_required": 2, "is_moe": False},
    {"name": "Llama-3-70B", "parameters": 70.0, "quantized": False, "ram_required": 140, "is_moe": False}, # Fails: too much RAM
    {"name": "Mixtral-8x7B", "parameters": 47.0, "quantized": True, "ram_required": 24, "is_moe": True},  # Fails: is_moe is True
    {"name": "Qwen2.5-7B", "parameters": 7.0, "quantized": True, "ram_required": 6, "is_moe": False},
    {"name": "TinyLlama-1.1B", "parameters": 1.1, "quantized": False, "ram_required": 4, "is_moe": False}
]
def find_playable_models(models):
    valid_models = []
    for model in models:
        if not model["is_moe"] and model["ram_required"] <= 8 and (model["quantized"] == True or model["parameters"] < 2):
            valid_models.append(model["name"])
    return valid_models
print(find_playable_models(available_models))

programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
print(programming_languages.index('Python', 3))
developer_names = ['Jess', 'Naomi', 'Tom']

# the break statement loops
for developer in developer_names:
    if developer == 'Naomi':
        break
    print(developer)
developer_names = ['Jess', 'Naomi', 'Tom']
# the continue statement in loops .
for developer in developer_names:
    if developer == "naomi":
        continue
    print(developer)

# the clear understanding of the break statement.
words = ['sky', 'apple', 'rhythm', 'fly', 'orange']

for word in words:
    for letter in word:
        if letter.lower() in 'aeiou':
            print(f"'{word}' contains the vowel '{letter}'")
            break
    else:
        print(f"'{word}' has no vowels")

""" hai in this code what are the benefits we get here by using the break statement is that here if in the we get any vowel letter in the 
 word the loop break on that particular word we get that the word contains the vowel if it dos,t contain the output we get the word dosen't contain the 
 vowel and the loop quite working aganin and again in this form so just go with it """

# the zip function

vegetables = ["banana","carrot","potato","onion"]
for index, vegetable in enumerate(vegetables):
    print(f"vegetable '{vegetable}'index {index}")

#   the dictionaries
pizza = {
    'name': 'Margherita Pizza',
    'price': 8.9,
    'calories_per_slice': 250,
    'toppings': ['mozzarella', 'basil']
}

# to access the key value pair"

print(pizza["name"])
pizza['name'] = "Margherita "
print(pizza["name"])

# the .get, operator

print(pizza.get("toppings",[]))
print(pizza.keys())
print(pizza.values())
print(pizza.items())
changes =  pizza.pop("price",10)
print(changes)

# what are some common techniques to loop over a dictionary

products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}
""" for iterating the for loop over prices of our products we can go in this way"""
for rates in products.values():
    print(rates)
# for iterating the for loop over keys.

for product in products.keys():
    print(product)

# when we need to iterate over both the key and the value pairs .

for product,values in products.items():
    print(product,values)

# what if we have to iterate the discount of about 25 percent on our products.

for product,price in products.items():
    products[product] = round(price*0.5)
print(products)

# hai lets discuss that what are sets and how do they work
my_set = {1,2,3,4,5,6,7}
our_set = {1,4,6,7,9,0,3}

set_difference = set()
set_difference.add(frozenset(my_set & our_set))
print(set_difference)

the_exceptional_elements = my_set ^ our_set
print(the_exceptional_elements)

print(my_set.isdisjoint(our_set))
print(our_set.issubset(my_set))

watch_minutes = {
    "Attack on Titan": 120,
    "Vinland Saga": 45,
    "Bleach": 200,
    "Hell's Paradise": 30
}
for key,value in watch_minutes.items():
    watch_minutes[key] = round(value/60)
print(watch_minutes)

phonk_tracks = {
    "Midnight Drift": 165,
    "Shadow Strike": 130,
    "Neon Blood": 105,
    "Tokyo Grime": 155
}
def normalize_bpm(phonk_tracks):
    for key,value in phonk_tracks.items():
        phonk_tracks[key] = (value)
        if value > 150:
            phonk_tracks[key] = value-20
        elif value < 120:
            phonk_tracks[key] = value + 20

    return phonk_tracks
print(normalize_bpm(phonk_tracks))

kage_anime_users = {
    "User_Abhishek": {"watch_minutes": 850, "tier": "free", "show_ads": True},
    "User_Rahul": {"watch_minutes": 120, "tier": "free", "show_ads": True},
    "User_Zoro": {"watch_minutes": 600, "tier": "premium", "show_ads": False},
    "User_Levi": {"watch_minutes": 45, "tier": "free", "show_ads": True}
}
def update_user_tiers(kage_anime_users):
    for user, data in kage_anime_users.items():

        # Rule 1: Upgrade to VIP (You nailed the if statement!)
        if data["watch_minutes"] > 500 and data["tier"] == "free":
            kage_anime_users[user]["tier"] = "vip"
            kage_anime_users[user]["show_ads"] = False  # <- Added the ad removal

        # Rule 2 & 3: Demote if inactive, BUT protect Premium users!
        elif data["watch_minutes"] < 50 and data["tier"] != "premium":
            kage_anime_users[user]["tier"] = "inactive"

    return kage_anime_users


# Print the final result
print(update_user_tiers(kage_anime_users))









