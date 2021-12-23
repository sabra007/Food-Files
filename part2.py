import json

with open('food_file.json') as f:
    data = json.load(f)
    food_items = (data)


# Complete the following items:

# Read in the JSON from the Food Files Exercise Part 1 into a dictionary.

# Count the number of low fat, high fiber, and low glycemic foods and print the statistics to the screen.
recommended_foods = []

for item in food_items:
    if item['low fat'] == 'yes' and item['low glycemic index'] == 'yes' and item['high fiber'] == 'yes':
        recommended_foods.append(item)
        
print(f"There are {len(recommended_foods)} low fat, high fiber, and low glycemic foods\n")


# Calculate the percentage of foods that are low fat, high fiber and low glycemic foods.
prc = len(recommended_foods)/len(food_items) * 100

print(f"{prc} % of foods are low fat, high fiber and low glycemic foods.\n")
# Print out all foods that are low fat, high fiber, and low glycemic foods using f strings and telling the system users that these are recommended foods.
# For example: Strawberry is a recommend food.

for food in recommended_foods:
    print(f"{food['foods']} is a recommended food")