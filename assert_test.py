import unittest
#引入测试类或者模块
from city_functions import City

#继承unittest.TestCase类
class NamesTestCase(unittest.TestCase):
	'''测试名称'''
	#准备工作
	def setUp(self):
		self.city=City()

	def test_city_name(self):
		#测试方法以test_开头
		name=self.city.get_name('北京','中国')
		print(name)
		self.assertEqual(name,'北京:中国')

	def test_city_score(self):
		score=self.city.get_name_score('北京','中国',10)
		self.assertEqual(score,'北京:中国--10')

#运行测试代码
unittest.main()