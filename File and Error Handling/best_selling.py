import csv

# Step 1: Open the original CSV file in read mode
with open('Bestseller - Sheet1.csv', 'r', encoding='utf8') as file:
    reader = csv.reader(file)
    
    # Read the header row first
    header = next(reader)
    
    # Assuming there's a column named 'Sales in millions'
    sales_index = header.index('sales in millions')
    
    # Initialize variables to track the bestseller
    bestseller = None
    highest_sales = 0
    
    # Step 2: Loop through each row to find the highest sales
    for row in reader:
        try:
            sales = float(row[sales_index])
            if sales > highest_sales:
                highest_sales = sales
                bestseller = row
        except ValueError:
            # Skip rows where sales are not numbers
            continue

# Step 3: Create a new CSV file to store the bestseller info
with open('bestseller_info.csv', 'w', newline='') as new_file:
    writer = csv.writer(new_file)
    
    # Write header and the bestseller row
    writer.writerow(header)
    writer.writerow(bestseller)

print("Bestseller information saved to 'bestseller_info.csv'")
print("Book details:", bestseller)
