from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    biggest_score = 0
    name = ""
    for x, y in scores:

        if y > biggest_score:
            biggest_score = y
            name = x

    return name


# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
