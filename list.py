#使用[]表示列表
names=["zdy","xyh","zs"]
print(names[0]+"\n"+names[1]+"\n"+names[2])
print("----"+names[2])
names[2]="ls"
print(names[0]+"\n"+names[1]+"\n"+names[2])
print("---------------")
#a.insert(索引，值)在列表中插入值
#append在末尾追加

names.insert(0,"kt")
names.insert(2,"zj")
names.append("mw")
print(names)
print("--------------")
#使用-1 -2表示倒第几个
print(names.pop(-1))
print(names.pop(-1))
print(names.pop(-1))
print(names.pop(-1))
print(names)
print('------------')
#删除 del a[1]
#删除并使用 a.pop(1)
#删除末尾 a.pop()
#删除某值 a.remove(val)
del names[1]
print(names)
names.remove('kt')
print(names)

names=["zdy","xyh","zs"]
#对列表进行永久性排序 a.sort()
#倒排 a.sort(reverse=True)
#临时性排序 sorted(a)
#临时排序，倒排 sorted(a,reverse=True)
names.sort()
print(names)
names.sort(reverse=True)
print(names)
print('----')
print(sorted(names))
print(names)
print('----')
print(sorted(names,reverse=True))


print('=====')
#reverse永久性反转
names.reverse()
print(names)
print(names.reverse())

#len(a) 列表的长度
print(len(names))

print("*"*100)
yuanzu= (1,2,3)
zidian = {'1':'a'}


