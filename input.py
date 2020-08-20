#用户输入,sublime 无法运行，需使用终端 python input.py
message=input('请输入名称：')
print('你的名称是：'+message)

#输入多行，使用\n
prompt = "If you tell us who you are, we can personalize the messages you see." 
prompt += "\nWhat is your first name? "
name = input(prompt)
print("\nHello, " + name + "!")

#编写一个程序，询问用户有多少人用餐。如果超过 8 人，就打印一 条消息，指出没有空桌;否则指出有空桌
#-----int()-----
person=input('please tell me , what person do you have ?')
person=int(person)
if person > 8:
	print('目前没有空的座位')
else:
	print('有空桌')

#取模%
num=input('判断该数是奇数还是偶数：')
num=int(num)
if num % 2 == 0:
	print('偶数')
else:
	print('奇数')