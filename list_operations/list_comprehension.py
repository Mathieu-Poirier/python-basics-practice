from typing import List


def create_list_of_odds(n: int) -> List[int]:
    result = [i for i in range(1, n + 1) if i % 2 != 0]
    return result


# want to add i to the list -> loop i in i in (iterator) if condition
# better solution: return [i for i in range(1, n + 1, 2)]
# do not modify below this line
print(create_list_of_odds(1))
print(create_list_of_odds(5))
print(create_list_of_odds(6))
print(create_list_of_odds(10))
