
arraysort = list(map(str, input("정수 입력 : ").split()))
n = len(arraysort)
for i in range(n):
     for j in range(n):
         if arraysort[i]>arraysort[j]:
             arraysort[i], arraysort[j] = arraysort[j], arraysort[i]
print(arraysort)