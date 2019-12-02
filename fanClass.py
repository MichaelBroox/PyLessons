class Fan(object):
	def __init__(self, SLOW=1, MEDIUM=2, FAST=3, speed=None, on=None, radius=None, color=None):
		self.SLOW = SLOW

		self.MEDIUM = MEDIUM
		
		self.FAST = FAST
		
		if  speed is None:
			self.__speed = SLOW
		else:
			self.__speed = speed

		if on is None:
			self.__on = False
		else:
			self.__on = on
		
		if radius is None:
			self.__radius = 5
		else:
			self.__radius = radius

		if color is None:
			self.__color = 'Blue'
		else:
			self.__color = color

	def set_speed(self, speed): # Mutator method for fan speed
		self.__speed = speed

	def get_speed(self):
		return self.__speed # Accessor method for fan speed

	def set_on(self, on): # Mutator method for fan status
		self.__bool = bool

	def get_on(self): # Accessor method for fan status
		return self.__on

	def set_radius(self, radius): # Mutator method for fan radius
		self.__radius = radius

	def get_radius(self): # Accessor method for fan radius
		return self.__radius

	def set_color(self, color): # Mutator method for fan color
		self.__color = color

	def get_color(self): # Accessor method for fan color
		return self.__color

