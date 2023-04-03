
def selection_sort(array):
    n = len(array)
    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_index = i
        for j in range(i+1, n):
            if array[j] < array[min_index]:
                min_index = j
        # Swap the found minimum element with the first element       
        array[i], array[min_index] = array[min_index], array[i]
    return array
array = [64, 25, 12, 22, 11]
sorted_array = selection_sort(array)
print(sorted_array)
