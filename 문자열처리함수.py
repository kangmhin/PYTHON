# PYTHON
python = "Python is Amazing"
print(python.lower()) #소문자로 출력
print(python.upper()) #대문자로 출력
print(python[0].isupper()) #python의 0번째 값이 대문자인지 True/False
print(len(python)) #length
print(python.replace("Python", "Java")) #교체

index = python.index("n")
print(index)
index = python.index("n", index+1)
print(index)

print(python.find("n"))
print(python.find("Java")) #print(python.index("Java")) << 오류남

print(python.count("n"))
