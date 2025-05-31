import timeit
import random

# Insertion (use github for more information)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# Merge

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    merged = []
    left_index, right_index = 0, 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged


# Timsort

def tim_sort(arr):
    return sorted(arr)


# Array for testing

size = 10000
array_for_test = [random.randint(0, 10000) for _ in range(size)]


# Time for algorithms (use hint)

insertion_time = timeit.timeit(
    lambda: insertion_sort(array_for_test.copy()), number=10000)
merge_time = timeit.timeit(lambda: merge_sort(array_for_test.copy()), number=10000)
timsort_time = timeit.timeit(lambda: tim_sort(array_for_test.copy()), number=10000)

# Result of timing
print(f"Insertion Sort Time(insertion_time): {insertion_time:.6f} seconds")
print(f"Merge Sort Time(merge_time): {merge_time:.6f} seconds")
print(f"Timsort Time(timsort_time): {timsort_time:.6f} seconds")
