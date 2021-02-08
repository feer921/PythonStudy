# 使用 bool 内置类可以将其他数据类型转换成为布尔值

print(bool(100))  # --> True
print(bool(-1))  # --> True

print(bool(0))  # --> False

#  即只有 数字 0转换成 布尔值为 False,其他的为 True

print(bool('hello'))  # --> True

print(bool('False'))  # --> True

print(bool(''))  # --> False

#  字符串里只有 空字符串 '' 或者 "" 转换成为 False，其他的字符串都是 True

#  None 转换成布尔值是 False
print(bool(None))  # --> False

print(bool("None"))  # --> True

print(bool([]))  # --> False 其中 []为空列表

print(bool(()))  # --> False 其中 ()为空 元组

print(bool({}))  # --> False 其中 {} 为空 字典

s = set()  # --> 空集合

print(bool(s))  # --> False

#  总结： 数字0，空字符串，空集合set()、空列表[]、空元组()、空字典{}、空数据 None,会被转换为 False

#  在计算机里， True 和 False 其实就是使用 1 和 0 来保存的

print(True + 1)  # --> 2

print(False + 1)  # --> 1

#  隐式类型转换
if 3 > 2:   # 3 > 2隐式转换为  True了
    print('hello')

if 0:   # 0 被隐式转换为 False 了
    print("error")

    





