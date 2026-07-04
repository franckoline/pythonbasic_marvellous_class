import csv

def load_data(filename):
    data = []
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['item'] = str(row['item'])
            row['quantity'] = int(row['quantity'])
            row['price'] = int(row['price'])
            data.append(row)
        # print(data)
    return data

def calculate_total_sales(data):
    grand_total = 0
    for row in data:
        total = row['quantity'] * row['price']
        row['total_sales'] = total
        grand_total += total
    return grand_total

def get_best_seller(data):
    best_item = data[1]
    for row in data:
        if row['quantity'] > best_item['quantity']:
            best_item = row
    return best_item

def filter_expensive_items(data, threshold):
    filtered_list = [row for row in data if row['price'] > threshold]
    return filtered_list

def save_report_to_txt(filename, total, best_item, filtered_data):
    """Writes the final results into a text file."""
    with open(filename, mode='w') as file:
        file.write("--- SALES SUMMARY REPORT ---\n")
        file.write(f"Total Revenue: {total}\n")
        file.write(f"Best Selling Item: {best_item['item']}\n")
        file.write("\n--- EXPENSIVE ITEMS ---\n")
        for item in filtered_data:
            file.write(f"- {item['item']}: {item['price']}\n")
    print(f"Report successfully saved to {filename}")