# # use heapq take from google

# import heapq

# def merge_k_lists(lists):
#     return list(heapq.merge(*lists))

# # 📌 Тестовий приклад
# lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
# merged_list = merge_k_lists(lists)

# #Result
# print("Sorted list:", merged_list)


# # use conspect and google

# def merge_two_lists(list1, list2):
#     merged = []
#     i, j = 0, 0
#     while i < len(list1) and j < len(list2):
#         if list1[i] <= list2[j]:
#             merged.append(list1[i])
#             i += 1
#         else:
#             merged.append(list2[j])
#             j += 1
#     merged.extend(list1[i:])
#     merged.extend(list2[j:])
#     return merged

# def merge_k_lists(lists):
#     if not lists:
#         return []
#     while len(lists) > 1:
#         merged_lists = []
#         for i in range(0, len(lists), 2):
#             list1 = lists[i]
#             list2 = lists[i+1] if i+1 < len(lists) else []
#             merged_lists.append(merge_two_lists(list1, list2))
#         lists = merged_lists
#     return lists[0]

# # 📌 Тестовий приклад
# lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
# merged_list = merge_k_lists(lists)

# # Вивід результату
# print("Відсортований список використовуючи рекурсію:", merged_list)