import heapq
from typing import List


def get_min_element(arr: List[int]) -> int:
    return heapq.nsmallest(1, arr)[0]


def get_min_4_elements(arr: List[int]) -> List[int]:
    # Return elements in *increasing* order
    return heapq.nsmallest(4, arr)


def get_min_2_elements(arr: List[int]) -> List[int]:
    # Return elements in *decreasing* order
    return sorted(heapq.nsmallest(2, arr), reverse=True)


# do not modify below this line
print(get_min_element([1, 2, 3]))
print(get_min_element([3, 2, 1, 4, 6, 2]))
print(get_min_element([1, 9, 7, 3, 2, 1, 4, 6, 2]))
