from typing import List


def disallow_negatives(num: int) -> int:
    return max(0, num)


def max_difference(nums: List[int]) -> int:
    ret = 0
    for i in range(len(nums) - 1):
        ret = max(ret, nums[i + 1] - nums[i])
        print(f"nums[i] + 1 = {i + 1}")
    return ret


# do not modify below this line

print(max_difference([1, 2, 3, 4, 5, 6, 7, 8, 9]))
