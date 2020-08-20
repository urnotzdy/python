class City():
	"""拼接城市名称"""
	def get_name(self,city,country):
		 return city+":"+country

	def get_name_score(self,city,country,score=0):
		return city+":"+country+"--"+str(score)