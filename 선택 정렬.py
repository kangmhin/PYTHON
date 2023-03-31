
arraysort = list(map(str, input("정수 입력 : ").split()))
n = len(arraysort)
for i in range(n):
     for j in range(0, n-i-1):
         if arraysort[j]>arraysort[j+1]:
             arraysort[j], arraysort[j+1] = arraysort[j+1], arraysort[j]
for i in range(n):
    print(arraysort[i], end = " ")