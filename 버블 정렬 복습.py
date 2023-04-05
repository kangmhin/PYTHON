def arraysort(array):
    n = len(array)
    for i in range(n-1):
        for j in range(n-i-1):
            if array[j]>array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array
array = list(map(int, input("정수 입력 : ").split()))
arraysort(array)
print(array)