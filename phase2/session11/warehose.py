import numpy as np

# --- STEP 1: Designing the 2D Inventory Matrix ---
# Rows = Warehouses (Yola, Abuja, Lagos)
# Columns = Product Categories (Laptops, Tablets, Routers, Screens)
# Values = Base Cost Price (in Thousands of Naira)

inventory_matrix = np.array([
    [350, 120, 45, 85],   # Warehouse 1: Yola Inventory
    [380, 130, 40, 90],   # Warehouse 2: Abuja Inventory
    [340, 115, 48, 80]    # Warehouse 3: Lagos Inventory
])

print("--- Initial Regional Inventory Cost Matrix (in ₦'000) ---")
print(inventory_matrix)
print(f"Matrix Dimensions (Rows, Columns): {inventory_matrix.shape}")
print(f"Total Dimensions Count (Rank):      {inventory_matrix.ndim}\n")


# --- STEP 2: Defining the Categorical Adjustments ---
# We have 4 unique tax markup multipliers—one for each product category:
# Laptops +15% (1.15), Tablets +10% (1.10), Routers +5% (1.05), Screens +20% (1.20)
category_multipliers = np.array([1.15, 1.10, 1.05, 1.20])

print("--- 1D Category Adjustment Vector ---")
print(category_multipliers)
print(f"Vector Shape: {category_multipliers.shape}\n")


# --- STEP 3: Executing Matrix Broadcasting ---
# NumPy detects that the matrix has 4 columns and the vector has 4 items.
# It automatically broadens the vector down all 3 rows simultaneously.
final_retail_prices = inventory_matrix * category_multipliers

print("--- Final Calculated Retail Price Matrix (Tax Inclusive) ---")
# Rounding for clean visual formatting
print(np.round(final_retail_prices, 2))


# --- STEP 4: Matrix Reductions & Aggregations ---
print("\n--- Business Intelligence Insights ---")

# Calculate total asset value sitting in each warehouse (Sum along rows / Axis 1)
warehouse_totals = final_retail_prices.sum(axis=1)
print(f"Total Portfolio Value by Warehouse (Yola, Abuja, Lagos): {np.round(warehouse_totals, 2)}")

# Calculate the average price for each product category across the country (Mean down columns / Axis 0)
category_means = final_retail_prices.mean(axis=0)
print(f"National Average Retail Price by Category (Laptops, Tablets, Routers, Screens): {np.round(category_means, 2)}")