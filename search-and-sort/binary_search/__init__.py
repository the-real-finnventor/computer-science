from typing_extensions import SupportsIndex


def binary_search(sorted_list: list, value) -> SupportsIndex:
    curr_index: SupportsIndex = (len(sorted_list) / 2).__floor__()
    new_sorted_list = sorted_list.copy()
    while new_sorted_list[curr_index] != value:
        if new_sorted_list[curr_index] > value:
            new_sorted_list = new_sorted_list[:curr_index]
        elif new_sorted_list < value:
            new_sorted_list = new_sorted_list[curr_index:]
            del new_sorted_list[0]
        if len(new_sorted_list) == 0:
            return -1
        curr_index: SupportsIndex = (len(new_sorted_list) / 2).__floor__()
    return curr_index
