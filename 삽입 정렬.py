def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if array[j-1]>array[j]:
                array[j-1], array[j]=array[j], array[j-1]
    return array
array = list(map(int, input("정수입력 : ").split()))
insertion_sort(array)
print(array)

