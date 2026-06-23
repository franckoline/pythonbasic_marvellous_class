import time
import numpy as np

long_list = []
for i in range(1000001):
    long_list.append(i)

start_time = time.time()
for i in range(len(long_list)):
    long_list[i] *= 4


total_time = time.time() - start_time
print(total_time)

long_list1 = np.array(long_list)

start_time1 = time.time()
for i in range(len(long_list)):
    long_list1 *= 4

total_time1 = time.time() - start_time1
print(total_time1)



