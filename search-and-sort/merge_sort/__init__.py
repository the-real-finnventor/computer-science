def merge(sorted_list_1: list, sorted_list_2: list) -> list:
    rv: list = []
    while sorted_list_1 or sorted_list_2:
        if len(sorted_list_1) == 0:
            rv.append(sorted_list_2.pop(0))
        elif len(sorted_list_2) == 0:
            rv.append(sorted_list_1.pop(0))
        elif sorted_list_1[0] < sorted_list_2[0]:
            rv.append(sorted_list_1.pop(0))
        elif sorted_list_1[0] > sorted_list_2[0]:
            rv.append(sorted_list_2.pop(0))
        elif sorted_list_1[0] == sorted_list_2[0]:
            rv.append(sorted_list_1.pop(0))
    return rv


def merge_sort(unsorted_list: list) -> list:
    if len(unsorted_list) <= 1:
        return unsorted_list
    halfway = len(unsorted_list) // 2
    return merge(merge_sort(unsorted_list[:halfway]), merge_sort(unsorted_list[halfway:]))
