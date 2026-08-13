import time
import numpy as np

# Let generate a standard Python list with 1 million mock transaction amounts
# Let generate a standard Python list with 1 million mock transaction amounts
# Let generate a standard Python list with 1 million mock transaction amounts
large_python_list = list(range(1, 1000001))

# Our Task: We are to apply a 10% inflation adjustment adjustment across all values

# Native Python Loop
start_time = time.time()
python_result = [price * 1.10 for price in large_python_list]
python_duration = time.time() - start_time

# Vectorized NumPy Array
# 1. Convert the standard Python list into a high-speed 1D NumPy array
numpy_array = np.array(large_python_list)

start_time = time.time()
# Vectorized Math: No loops required!
numpy_result = numpy_array * 1.10
numpy_duration = time.time() - start_time

print("--- Performance Analytics ---")
print(f"Standard Python List Loop: {python_duration:.5f} seconds")
print(f"Vectorized NumPy Array:     {numpy_duration:.5f} seconds")
# print(f"NumPy speed factor improvement: {python_duration / numpy_duration:.1f}x faster\n")


# --- STEP 2: Creating and Slicing Arrays ---
print("--- Array Manipulation & Slicing Matrix ---")

# Create a clean, manual 1D array of daily target revenues (in Thousands)
revenue_grid = np.array([120, 150, 95, 210, 88, 175, 300])
print(f"Original Revenue Grid: {revenue_grid}")
print(f"Array Shape: {revenue_grid.shape} | Data Type: {revenue_grid.dtype}")

# Slicing Exercises (Extracting specific data subsets)
# Syntax: array[start:stop:step]

# 1. Extract the first 3 days of revenue (Index 0 up to 3)
first_three_days = revenue_grid[0:3]
print(f"First Three Days:      {first_three_days}")

# 2. Extract weekend performance (The final 2 elements using negative indexing)
weekend_performance = revenue_grid[-2:]
print(f"Weekend Performance:   {weekend_performance}")

# 3. Every alternate day (Step slicing)
alternate_days = revenue_grid[::2]
print(f"Alternate Days:        {alternate_days}")

"""
Simple Project on 
"""
# 1. Simulate raw tracking data for 100,000 Nigerian MSMEs
# Generating random revenues between ₦50,000 and ₦1,500,000
import random
random.seed(42) # Ensure consistent data across all student screens
raw_msme_revenues = [random.randint(50000, 1500000) for _ in range(100000)]

print(f"Loaded {len(raw_msme_revenues)} MSME records into a standard Python list.")

# --- Method A: Standard Python Loop ---
start_py = time.time()
usd_list_py = [ngn / 1500 for ngn in raw_msme_revenues]
duration_py = time.time() - start_py

# --- Method B: NumPy High-Speed Vectorization ---
# Step 2a: Convert native list into a 1D NumPy Array
np_msme_revenues = np.array(raw_msme_revenues)

start_np = time.time()
# Step 2b: Vectorized division (happens instantly in memory)
usd_array_np = np_msme_revenues / 1500
duration_np = time.time() - start_np

print(f"Python Loop Time: {duration_py:.5f} seconds")
print(f"NumPy Vector Time: {duration_np:.5f} seconds")
print(f"🚀 Performance Boost: {duration_py / duration_np:.1f}x faster using NumPy!")

print("\n--- Auditing Data Quality via Slicing ---")

# Task 1: Extract the first 5 MSME records from the NumPy array
sample_start = np_msme_revenues[:5]
print(f"First 5 MSME Revenues (NGN): {sample_start}")

# Task 2: Extract the last 3 MSME records using negative indexing
sample_end = np_msme_revenues[-3:]
print(f"Last 3 MSME Revenues (NGN):  {sample_end}")

# Task 3: Extract a specific batch (e.g., records 500 to 505)
sample_batch = np_msme_revenues[500:505]
print(f"Batch Sample [500:505]:      {sample_batch}")

print("\n--- Grant Eligibility Extraction ---")

# Step 4a: Create a boolean filter condition mask
subsidy_mask = np_msme_revenues < 250000

# Step 4b: Pass the mask directly into the array to pull matching values
eligible_msmes = np_msme_revenues[subsidy_mask]

total_eligible = len(eligible_msmes)
percentage = (total_eligible / len(np_msme_revenues)) * 100

print(f"Total MSMEs qualifying for MIH subsidy: {total_eligible}")
print(f"Percentage of vulnerable MSMEs: {percentage:.2f}%")