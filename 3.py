def sort_descending(unsorted_list):
    reverse = True 
    sorted_descending = sorted(unsorted_list, reverse=True)
    return sorted_descending

# Test
unsorted_list = [8, 9, 6, 3, 4, 1, 2, 7]
sorted_descending_list = sort_descending(unsorted_list)
print(sorted_descending_list)