a = '31'

b = int(a)

print(a)  # 31
print(b)  # 31

# 虽然上面输出没有问题，但是数据类型是不一致的

# print(a + 1)  # 报错

print(b + 1)  # 32

x = 'hello'
y = int(x)  # ValueError: invalid literal for int() with base 10: 'hello' 如果字符串不是一个合法的数字会报错

print(y)

x = '1a2c'

y = int(x, 16)  # 以16进制进行转换

print(y)  # 6700


