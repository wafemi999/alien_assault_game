class aa_stats():
	"""Keeping the statistics for alien assault"""
	
	def __init__(self, aa_settings):
		"""initialisation"""
		self.aa_settings = aa_settings
		self.reset_stats()
		self.game_active = False
		self.high_score = 0
		
		
	def reset_stats(self):
		"""keeps track of number of player's ship"""
		self.ship_left = self.aa_settings.ship_limit
		self.score = 0
		self.level	=1
