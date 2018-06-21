class Pet():
	"""Базовый класс, который будут наследовать все остальные домашние животные."""
	running_spead = 0  #km per hour
	mass = 0 #kg
	food_needed = 0 #kg
	life_expectancy = 0 #months
	space_needed = 0 #square meter 
	
	def __init__(self, name):
		"""Чтобы у каждого животного всегда было свое имя."""
		self.name = name
