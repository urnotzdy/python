# #使用def定义函数
# def	get_age(username):
# 	#'''参数定义'''
# 	print(username+' 的年龄是16')

# get_age("张三")

# #专辑
# #可以给形参指定默认值
# def make_album(gsname,zjname,num=0):
# 	ablum={'歌手名称':gsname,'专辑名称':zjname}
# 	if num:
# 		ablum['收录歌曲']=num
# 	return ablum

# while True:
# 	print('请输入专辑相关信息：')
# 	print("(enter 'q' at any time to quit)")
# 	gs=input('歌手名称：')
# 	if gs == 'q':
# 		break
# 	zj=input('专辑名称：')
# 	if zj == 'q':
# 		break
# 	num=input('收录歌曲：')
# 	if num == 'q':
# 		break
# 	print(make_album(gs,zj,num))

#传递列表--列表被修改
def liebiao(ls):
	ls[0]='修改'
	return ls

ls=['old1','old2']
liebiao(ls)
print(ls)

#传递列表--列表不被修改
ls=['old1','old2']
liebiao(ls[:])
print(ls)

#first,last 为位置实参
#user_info为关键字实参 **
#任意数量的实参 *
def build_profile(first, last, **user_info):
	"""创建一个字典，其中包含我们知道的有关用户的一切""" 
	profile = {}
	profile['first_name'] = first 
	profile['last_name'] = last
	for key,value in user_info.items():
		profile[key]=value
	return profile
print(build_profile('z','dy',age=10,sex='gril'))

def f(a,L=[]):
	L.append(a)
	return L
print(f(1))

