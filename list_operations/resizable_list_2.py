"""
These list operations are less common, but they are absolutely worth knowing:

    index(): Returns the index of the first occurrence of a specified element in the list.
        If the element is not in the list, we will get an ValueError.
    remove(): Removes the first occurrence of a specified element from the list.
    extend(): Adds the elements of another list to the end of the list.

"""

from typing import List


def append_elements(arr1: List[int], arr2: List[int]) -> List[int]:

    arr1.extend(arr2)

    return arr1


def remove_elements(arr1: List[int], arr2: List[int]) -> List[int]:

    for i in arr2:
        if i in arr1:
            arr1.remove(i)

    return arr1


# do not modify below this line
print(append_elements([1, 2, 3], [4, 5, 6]))
print(append_elements([4, 3], [4, 5, 3]))

print(remove_elements([1, 2, 3, 4, 5], [2, 4, 6]))
print(remove_elements([1, 2, 3, 4, 5], [2, 3, 4, 5, 5]))
print(remove_elements([1, 7, 2, 3, 4, 5], [6, 7, 8, 2]))
