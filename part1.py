import json

with open("foods.txt", "r") as my_file:
    food_content = (my_file.readlines())

with open("highfiber.txt", "r") as my_file:
    high_fiber_content = (my_file.readlines())
with open("low-glycemic-index.txt", "r") as my_file:
    low_glycemic_index_content = (my_file.readlines())

with open("lowfat.txt", "r") as my_file:
    lowfat_content = (my_file.readlines())


new_list = []
header = []

for content in [food_content, high_fiber_content, low_glycemic_index_content, lowfat_content]:
    
    header.append(content[0].strip())


for i in range(1, len(food_content)):
    
    food_item = {
        header[0]: food_content[i].strip().lower(), 
        header[1]: high_fiber_content[i].strip().lower(),
        header[2]: low_glycemic_index_content[i].strip().lower(),
        header[3]: lowfat_content[i].strip().lower()
    }
    new_list.append(food_item)


for item in new_list:
    print(f"{item}")

food_items = []    # final clean list

for item in new_list:
    if item not in food_items:
        if item[header[1]] == 'no' or item[header[1]] == 'yes':
            food_items.append(item)


print("clean items")
for item in food_items:
    print(f"{item}")

with open('food_file.json', 'w') as fout:
    json.dump(food_items , fout)