"""
Sorting a list using the built-in sort method

Prints list after sorting
>>> print(elements)
[1, 1, 3, 4, 5]

python -m doctest -v .\sort_ascending.py

Time: O(nlogn)
Space: O(n)
"""

elements = [1, 5, 3, 4, 1]
elements.sort()
