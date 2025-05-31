# import timeit
# import pandas as pd

# # 📌 Завантаження датасету (локальний файл)
# df = pd.read_csv("./top-rated-coffee-clean.csv")

# # 📌 Вибираємо колонку "total_score" для сортування
# coffee_scores = df["total_score"].dropna().tolist()

# # 📌 Сортування вставками
# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and arr[j] > key:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key
#     return arr

# # 📌 Сортування злиттям
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])
#     return merge(left, right)

# def merge(left, right):
#     merged = []
#     left_index, right_index = 0, 0
#     while left_index < len(left) and right_index < len(right):
#         if left[left_index] <= right[right_index]:
#             merged.append(left[left_index])
#             left_index += 1
#         else:
#             merged.append(right[right_index])
#             right_index += 1
#     merged.extend(left[left_index:])
#     merged.extend(right[right_index:])
#     return merged

# # 📌 Стандартний Timsort (Python sorted)
# def python_sorted(arr):
#     return sorted(arr)

# # 📌 Вимірювання часу виконання
# time_insertion = timeit.timeit(lambda: insertion_sort(coffee_scores.copy()), number=10)
# time_merge = timeit.timeit(lambda: merge_sort(coffee_scores.copy()), number=10)
# time_timsort = timeit.timeit(lambda: python_sorted(coffee_scores.copy()), number=10)

# # ✅ Вивід результатів
# print(f"Час виконання сортування вставками: {time_insertion:.6f} секунд")
# print(f"Час виконання сортування злиттям: {time_merge:.6f} секунд")
# print(f"Час виконання Timsort (Python sorted): {time_timsort:.6f} секунд")