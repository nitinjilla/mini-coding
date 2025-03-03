def rotate_list (input_list: list, rotation_constant: int = 1) -> list:

    if rotation_constant > len (input_list):
        raise Exception("Rotation constant cannot be greater than length of the list.")
    
    if rotation_constant == len(input_list):
        return input_list

    return input_list[rotation_constant:] + input_list[:rotation_constant]

# stupid me couldn't think that I had to just switch the slices. now I do.




