class Settings():
	'''this stores all settings for alien_assault'''
	
	def __init__(self):
		'''initialise variable for setings:'''
		self.screen_width = 800
		self.screen_height = 640
		self.bckg_color = (230,230,230)
		#Ship settings , 1 = right, -1 = left
		self.ship_speed_factor = 1.2
		self.ship_limit = 3
		
		#alien settings
		self.alien_speed_factor = 1
		self.aliens_drop_speed = 20
		self.aliens_direction = 1

		#bullet settings:
		self.bullets_speed_factor = 3
		self.bullet_width = 3
		self.bullet_height = 8
		self.bullet_color = 60, 60, 60
		self.bullet_allowed = 4
		
		
		
		self.speedup_scale = 1.2
		
		#alien point value increases with level
		self.score_scale = 1.5
		
		self.dynamic_settings()
		
		
	def dynamic_settings(self):
		"""settings that changes in the game"""
		self.ship_speed_factor = 1.5
		self.bullets_speed_factor = 3
		self.alien_speed_factor = 1
		self.aliens_direction = 1
		
		self.alien_points = 10
		
		
	def increase_speed(self):
		"""increase speed settings"""
		self.ship_speed_factor *= self.speedup_scale
		self.bullets_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		self.alien_points = int(self.alien_points * self.score_scale)
		
		
		
