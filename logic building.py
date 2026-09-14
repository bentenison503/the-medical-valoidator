# match_results = ['w','w','L','w','d']
# total_points = 0
# for result in match_results:
#     if match_results = w:
     #    total_points =+ 3
     # elif match_result = D:
     #     total_points =+1
     #else:
         #total_points =+0
# print(total_points)

"""city_results = ['W', 'W', 'D', 'W', 'W', 'W', 'L', 'W']

current_streak = 0
max_streak = 0
for result in match results:
    if result == 'w':
        current_streak = current_streak+1
        current_streak+1 = max_streak
    else:
    current_streak = 0
print(max_streak)"""

# the data cleanser.
scores = [42,80,30,90,50,10]
total= 0
pass_count = 0
for marks in scores:
    if marks >= 50:
        pass_count = pass_count +1
        total = total +marks
print(total/pass_count)

# the movie ticket calculator.
age = 10
day = "Tuesday"
price = 150

if age<12:
    price = 80
elif age >= 60:
    price = 100
if day == "Tuesday":
    price = price*0.2
print(price)

# the ecommerce holiday sale .
inventory = [
    {"id": 1, "name": "Laptop", "price": 1200.00, "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "Coffee Mug", "price": 15.50, "category": "Home", "in_stock": True},
    {"id": 3, "name": "Wireless Mouse", "price": 45.00, "category": "Electronics", "in_stock": False},
    {"id": 4, "name": "Headphones", "price": 200.00, "category": "Electronics", "in_stock": True},
    {"id": 5, "name": "Python Crash Course", "price": 30.00, "category": "Books", "in_stock": True},
    {"id": 6, "name": "Monitor", "price": 300.00, "category": "Electronics", "in_stock": True}
]
def process_holiday_sale(products,discount_percentage):
    def pin_extractor(poem):
        secret_code = ''

    poem = """Stars and the moon
    shine in the sky
    white and bright
    until the end of the night"""

    pin_extractor(poem)
    valid_items = list(filter(lambda product: product["category"] == "Electronics", products))