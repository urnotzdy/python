# 字典---类似于map，以key-val进行存储，{}
person = {'name': 'zdy', 'age': 18}
print(person)
# 访问
print(person['name'])
# 添加
person['address'] = '北京'
print(person)
# 删除
del person['address']
print(person)
# 对象
laguage = {
    'zs': '中文',
    'ls': '英语'
}
print(laguage)

# 遍历对象--键值、键、值
# 键值 items()
for key, val in person.items():
    print("key:" + key + ",val:" + str(val))
# 字典推导式
tds = {"key:" + key + ",val:" + str(val) for key, val in person.items()}
print("==========")
print(tds)

# 值 keys()
for key in person.keys():
    print("key:" + key)
# 值 values()
for val in person.values():
    print("val:" + str(val))
# 去重
ls = ['s', 'a', 's']
print(set(ls))
# 排序
print(sorted(ls))
print(ls)
print(ls.sort())
print(ls)


# 嵌套
# 字典中嵌套列表、字典
# 列表中嵌套字典

def test_zd(m, n):
    print(m + ":" + n)


# **zd将字典转为key-value的列表
zd = {"m": "a", "n": "b"}

test_zd(**zd)
