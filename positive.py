def get_positive_element(input_list):
    output_list = []
    for x in input_list:
        if x > 0:
            output_list.append(x)
    return output_list

list1 = [12, -7, 5, 64, -14]
output1 = get_positive_element(list1)
print(output1)

list2 = [12, 14, -95, 3]
output2 = get_positive_element(list2)
print(output2)
