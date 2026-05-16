from function import load_data, calculate_total_sales, get_best_seller, filter_expensive_items, save_report_to_txt

# 1.
sales_list = load_data('sales_data.csv')
filename = "summary.txt"
# 2.
grand_total = calculate_total_sales(sales_list)

# 3.
best_selling_row = get_best_seller(sales_list)

# 4.
filter_figure = int(input("Enter Filter sales value: "))
expensive_items = filter_expensive_items(sales_list, filter_figure)

# 5.
print("--- SALES REPORT ---")
print(f"Grand Total Sales Revenue: {grand_total}")
print(f"Best Selling Item: {best_selling_row['item']} ({best_selling_row['quantity']} units)\n")

print(f"\n--- ITEMS PRICED OVER {filter_figure} ---")
for item in expensive_items:
    print(f"- {item['item']}: {item['price']}")

save_report_to_txt(filename, grand_total, best_selling_row, expensive_items)


