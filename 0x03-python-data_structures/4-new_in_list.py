#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if (not (my_list) or idx < 0 or idx >= len(my_list)):
        return my_list

    # copying
    new_list = my_list.copy()
    # Modify
    new_list[idx] = element
    return new_list
