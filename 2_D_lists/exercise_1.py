from typing import List


def find_max_in_each_list(nested_arr: List[int]) -> List[int]:

    max_element_in_sublist = []

    for i in nested_arr:
        max_element_in_sublist.append(max(i))

    return max_element_in_sublist


# do not modify below this line
print(find_max_in_each_list([[1, 2], [3, 4, 2]]))
print(find_max_in_each_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(find_max_in_each_list([[5, 6, 2, 8], [9], [9, 10], [11, 10, 11]]))
