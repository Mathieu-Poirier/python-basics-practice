grid = [[0 for i in range(3)] for j in range(2)]

grid[0][0] = 1

print(grid)  # [[1, 0, 0], [0, 0, 0]]


from typing import List


def create_grid(rows: int, cols: int, value: int) -> List[List[int]]:
    result = [[value] * cols for _ in range(rows)]
    return result


# do not modify below this line
print(create_grid(2, 3, 0))
print(create_grid(3, 2, 1))
print(create_grid(4, 4, 4))
print(create_grid(1, 1, 5))
print(create_grid(1, 5, 5))
