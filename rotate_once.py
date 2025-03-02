def rotate_once(input_list: list) -> list:
    first_element = input_list[0]

    for i in range (1, len(input_list)):
        input_list[i-1] = input_list[i]
    
    input_list[len(input_list) - 1] = first_element

    return input_list


""" 
l = [1, 2, 3, 4, 5]
print(rotate_once(l))  #[2, 3, 4, 5, 1]
print(rotate_once(l))  #[3, 4, 5, 1, 2]
print(rotate_once(l))  #[4, 5, 1, 2, 3]
print(rotate_once(l))  #[5, 1, 2, 3, 4]
"""