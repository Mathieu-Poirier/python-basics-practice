"""
The key parameter in the built-in sort function accepts a function that returns a key used for sorting
(You can sort based on whatever function you can transform each element into (key, transform) pair

Tests:

>>> print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))
['watermelon', 'blueberry', 'zucchini', 'cherry', 'banana', 'apple', 'kiwi', 'pear']
>>> print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
[1, 2, -2, 2, -3, 4, -4, -5, 5, -6, 6, 7, 9, 11, -19]
"""

def get_word_length(word):
    return len(word)

def get_absolute_value(number):
    return abs(number)

def sort_words(words):
    words.sort(key=get_word_length, reverse=True)
    return words


def sort_numbers(numbers):
    numbers.sort(key=get_absolute_value)
    return numbers


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))