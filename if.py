import sys
# 条件表达式===》if 条件 ：

# 字符串比较，加‘’
car = 'subaru'
if car == 'subaru':
    print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
if car != 'audi':
    print("Is car == 'audi'? I predict False.")
print(car == 'audi')
# 数字比较
num = 1
if num == 1:
    print("num = 1")
else:
    print("num=2")
# 在列表中 in 和 not in
ls = ['a', 'b']
if 'a' in ls:
    print('a in list')
if 'c' not in ls:
    print('c not in list')
# 布尔表达式
b = True
if b:
    print('布尔测试')
# 多个条件 and or
if b and num == 1:
    print("多条件and" +
          "测试")
if b or num == 2:
    print('多条件or' +
          '测试')
# if-else和if-elif-else
if num == 2:
    print('num = 2')
elif num == 1:
    print('num=1')
# 判断列表不为空------**********************包含任意一个元素，则为ture****************
lsts = []
if lsts:
    print('列表不空的')
else:
    print('列表是空的')

ls = list(range(300))
for b in ls:
    if b is not ls[b]:
        print("常量池最大值为：", (b - 1))
        break

a = 0
print(id(a))
b = [1000, 1111]
print(id(b))
# print(a is b)

print(sys.getrefcount(a))