pizzas=["p1","p2","p3"]
#列表 for val in vals:
for pizza in pizzas:
	print(pizza+" , I like pepperoni pizza")
print("I really love pizza!")

nums=[]
#range(from,to) 随机产生数组
for val in range(1,21):
	nums.append(val)
print(nums)

#list()函数将range()的结果转成列表
print(list(range(1,21,2)))

#**几次方
#列表解析：将for循环和创建新元素的代码合并一行，并自动附加新元素
nums=[v**2 for v in range(1,10)]
print(nums)
nums=list(range(1,1000000))
#max min sum简单的统计
print(min(nums))
print(max(nums))
print(sum(nums))

print(list(range(3,30,3)))

nums=[v**3 for v in range(1,10)]
print(nums)
print(nums[2])

scores=[3,6,2,4,9,8,9]
scores.sort(reverse=True)
#[from:to]切片 
print(scores[:3])
print(scores[-3:0])
i=len(scores)/2
print(i)
#[:]复制
scores1=scores[:]
print(scores1)

scores1.append(1)
print(scores1)
print(scores)

for s in scores:

	for x in range(1,10):
		print(x)

# 元组：不可变的列表
# 不可改变某一个值，但可以给存储元组的变量赋值
yuanzu=(6,9,0)
print(yuanzu)

##set集合
setstr={'1','2','1'}
print(setstr)

byte=b"aw1"
print(byte.decode("utf-8"))

#取步长
xlabes = [i/2 for i in range(4,49)]
print(xlabes[::3])
print(min(xlabes))
print(max(xlabes))