import json

#文件
class OperateFile():
	'''获取文本文件的内容'''
	def __init__(self,path):
		print('开始读取文件')
		self.path=path

	def read(self):
		'''捕获异常 try-except-else'''
		try:
			with open(self.path) as file_obj:
				self.contents=file_obj.read()
		except FileNotFoundError:
			print('文件'+self.path+'找不到！！！')
			self.contents=''
			self.path='num.txt'
		else:
			print('文件'+self.path+'读取成功！！！')

	def get(self):
		print(self.contents.rstrip())

	def read_lines(self):
		'''读取每一行的内容'''
		with open(self.path) as file_obj:
			for line in file_obj:
				print(line.rstrip())

	def read_lines_oth(self):
		with open(self.path) as file_obj:
			self.contents_lines=file_obj.readlines()

	def write(self,filename,mode):
		'''写入文件 w为写入模式 a为追加模式'''
		with open(filename, mode) as file_object:
			file_object.write("I love programming.\n")

	def write_json(self,filename,mode,jsondata=[]):
		'''写入json'''
		with open(filename, mode) as file_object:
			json.dump(jsondata,file_object)

	def read_json(self,filename,mode):
		'''加载json'''
		with open(filename, mode) as file_object:
			self.jsondata=json.load(file_object)

ope_file=OperateFile('n1um.txt')
ope_file.read()
ope_file.get()

ope_file.read_lines()

ope_file.read_lines_oth()
for line in ope_file.contents_lines:
	print(line.rstrip())

#替换字符串内容
oldcontent='python语言'
oldcontent=oldcontent.replace('python','java')
print(oldcontent)

ope_file.write('programming.txt','w')
ope_file.write('programming.txt','a')

jsondata=[{"a":"12"},{"b":"23"}]
ope_file.write_json('json.txt','w',jsondata)
ope_file.read_json('json.txt','r')
print(ope_file.jsondata)



