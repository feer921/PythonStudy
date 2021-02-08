a = '12.34'
# 使用内置的 float 类可以将其他类型数据转换为 float 浮点数

b = float(a)
print(b + 1)

# 如果字符串不能被转换为有效的浮点数，会报错
# c = float('hello')
# print(c)

c = 101

print(float(c))  # 101.0

m = float("12")  # 将字符串转换为浮点数

n = float(12)  # 将整形数字转换成浮点数，虽然输出一致，但过程不一致

print(m, n)  # 虽然输出一致，但过程不一致

