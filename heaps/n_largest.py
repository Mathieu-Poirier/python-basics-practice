from typing import List
from sortedcontainers import SortedDict


sorted_dict = SortedDict({"a": 1, "b": 2, "c": 3, "d": 4})

print(sorted_dict.popitem())
