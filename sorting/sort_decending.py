"""
Sorting a list using the built-in sort method

Prints list after sorting
>>> print(elementsTwo)
[5, 4, 3, 1, 1]

python -m doctest -v .\sort_ascending.py

Time: O(nlogn)
Space: O(n)
"""

elementsTwo = [1, 5, 3, 4, 1]
elementsTwo.sort(key=None, reverse=True)
