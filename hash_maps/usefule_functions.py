from typing import Dict, List, Tuple


def get_dict_items(age_dict: Dict[str, int]) -> List[Tuple[str, int]]:
    m_list = [(i, j) for i, j in age_dict.items()]
    return m_list


# do not modify below this line
print(get_dict_items({"Alice": 25, "Bob": 30, "Charlie": 35}))
print(get_dict_items({"Alice": 25, "Bob": 30, "Charlie": 35, "David": 40}))
print(get_dict_items({"Bob": 30, "David": 40, "Charlie": 35, "Alice": 25, "Eve": 45}))
print(
    get_dict_items(
        {"Alice": 25, "Bob": 30, "Charlie": 35, "David": 40, "Eve": 45, "Frank": 50}
    )
)
