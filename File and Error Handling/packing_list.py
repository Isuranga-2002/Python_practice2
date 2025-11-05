import csv

data = [
  ['Item', 'Quantity'],
  ['Blender', 2],
  ['Posters', 30],
  ['Shoes', 2]
]

try:
    with open('packing_list.csv', 'r', encoding='utf8') as file:
        reader = csv.reader(file)

        for row in reader:
            print(row)

except FileNotFoundError:
    print("Packing list file not found. Creating a new one.")

    with open('packing_list.csv', 'w', newline='') as new_file:
        writer = csv.writer(new_file)

        writer.writerows(data)