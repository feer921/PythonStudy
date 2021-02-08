# 使用内置 类 [str] 可以将其他类型的数据转换成为字符串

a = 34
b = str(a)

print(a, b)  # 输出一致，但本质不一致

print(type(a))  # <class 'int'>

print(type(b))  # <class 'str'>


