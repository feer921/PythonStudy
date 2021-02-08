# 进制转换，将 int类型以不同的进制表现出来

# 类型转换 将一个类型的数据转换为其他类型的数据  int==>str  str==>int  bool==> int int==>float

age = input("请输入您的年龄：")
print(type(age))  # <class 'str'>
# print(age+1) # 会报错误，因为 接收到的用户输入，都是 [str]字符串类型；在python里，如果字符串和数字做 加法去处，会直接报错

# 应该 把字符串类型的变量 age 转换成为数字类型的 age

# 使用 [int]内置函数可以将其他类型的数据转换成整数
age = int(age)

print(type(age))  # <class 'int'>

print(age + 1)  # 这样就不会报错了
