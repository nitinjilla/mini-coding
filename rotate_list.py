def rotate_list (input_list: list, rotation_constant: int = 1) -> list:

    if rotation_constant > len (input_list):
        raise Exception("Rotation constant cannot be greater than length of the list.")
    elif rotation_constant == len(input_list):
         return input_list
    else:
        sliced_list = input_list[:rotation_constant]

        for i in range (0, (len(input_list) - rotation_constant)):
            input_list[i] = input_list[rotation_constant + i]
        
        [input_list.pop() for i in range(0, rotation_constant)]

        input_list.extend(sliced_list)

        return input_list
        
"""
pl = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

print(rotate_list(pl, 15)) [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(rotate_list(pl, 10)) [11, 12, 13, 14, 15, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(rotate_list(pl))     [12, 13, 14, 15, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(rotate_list(pl, 16)) Exception: Rotation constant cannot be greater than length of the list.   
"""

