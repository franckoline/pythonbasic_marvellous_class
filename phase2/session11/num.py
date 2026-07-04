# import time
import numpy as np

# long_list = []
# for i in range(1000001):
#     long_list.append(i)
#
# start_time = time.time()
# for i in range(len(long_list)):
#     long_list[i] *= 4
#
#
# total_time = time.time() - start_time
# print(f"time for normal python array {total_time}")
#
# long_list1 = np.array(long_list)
#
# start_time1 = time.time()
# long_list1*= 4
#
#
# total_time1 = time.time() - start_time1
# print(f"time for numpy array {total_time1}")
#
#
# print(total_time / total_time1)

#
# array = np.array([[[34,54,65,786], [12,64,65,87], [65,7,98,54]],
#                   [[3,5,6,78], [1,6,6,8], [6,0,9,5]],
#                   [[4,4,5,86], [2,4,5,7], [5,4,8,4]]])
#
#
# print(array[0:2,1])

# item array containing [Item ID, Current Price, Discount, Final Price].
items = ["PROD001", "PROD002", "PROD003", "PROD004"]

properties_of_items = np.array([[60000, 10, 0],
                  [20000, 0, 0],
                  [15000, 15, 0],
                  [43000, 5, 0]], dtype = float)


properties_of_items[:, 2] = properties_of_items[:, 0] - (properties_of_items[:, 0] * (properties_of_items[:, 1]/ 100))


n = 0
prices = []
for i in range(4):
    prices.append(properties_of_items[n: n + 1, 2])
    n += 1

print(prices)
for price in prices:
    print(list(price))
