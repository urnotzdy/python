# 9-1 餐馆:创建一个名为 Restaurant 的类，其方法__init__()设置两个属性: restaurant_name 和 cuisine_type。
# 创建一个名为 describe_restaurant()的方法和一个名为 open_restaurant()的方法，其中前者打印前述两项信息，而后者打印一条消息， 指出餐馆正在营业。
# 根据这个类创建一个名为 restaurant 的实例，分别打印其两个属性，再调用前述 两个方法。
class Restaurant():
	#init是两个_
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name=restaurant_name
		self.cuisine_type=cuisine_type
	def describe_restaurant(self):
		print(self.restaurant_name+":"+self.cuisine_type)
	def open_restaurant(self):
		print("餐馆正在营业")

restaurant=Restaurant("一铁锨",'---1')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

#继承
class NewRestaurant(Restaurant):
	def __init__(self,restaurant_name,cuisine_type):
		#不传入self
		super().__init__(restaurant_name,cuisine_type)
newRestaurant=NewRestaurant("黄焖鸡","---2")
print(newRestaurant.restaurant_name)