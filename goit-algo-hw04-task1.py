import random
import timeit
import pandas as pd

# Implementation of the insertion sort algorithm
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Implementation of the merge sort algorithm
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

# Function to generate different types of data sets: random, sorted, and reverse sorted
def generate_data_sets(size):
    random_list = [random.randint(0, 1000) for _ in range(size)]
    sorted_list = sorted(random_list)
    reverse_sorted_list = sorted_list[::-1]
    return {'random': random_list, 'sorted': sorted_list, 'reverse_sorted': reverse_sorted_list}

# Function to measure the execution time for each algorithm
def measure_time(func, data):
    return timeit.timeit(lambda: func(data.copy()), number=1)

# Tests for various data sizes
sizes = [100, 1000, 5000, 10000]
results = []

# Collecting results for each size and type of data set
for size in sizes:
    data_sets = generate_data_sets(size)
    for data_type, data in data_sets.items():
        result = {
            'Data Size': size,
            'Data Type': data_type,
            'Insertion Sort': measure_time(insertion_sort, data),
            'Merge Sort': measure_time(merge_sort, data),
            'Timsort (sorted)': measure_time(sorted, data)
        }
        results.append(result)

# Creating DataFrame from results
df = pd.DataFrame(results)

# Displaying results in a table format
print(df)