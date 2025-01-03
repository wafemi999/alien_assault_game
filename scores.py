import pygame.font
from pygame.sprite import Group
from ship import Ship



class scores():
	
	"""A cass that keeps scoring info"""
	
	def __init__(self, aa_settings,screen,stats):
		"""initialize"""
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.aa_settings = aa_settings
		self.stats = stats
		
		self.text_color = (30,30,30)
		self.font = pygame.font.SysFont(None,25)
		
		self.prep_score()
		self.prep_high_score()
		self.prep_level()
		self.prep_ships()
		
		
	def prep_score(self):
		"""displays the score"""
		
		rounded_score = int(round(self.stats.score, -1))
		score_str = "SCORE:{:,}".format(rounded_score)
		self.score_image = self.font.render(score_str, True, 
			self.text_color, self.aa_settings.bckg_color)
			
		#displaying the score
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20
		
		
	def prep_high_score(self):
		''' makes highscore into an image'''
		high_score = int(round(self.stats.high_score, -1))
		high_score_str = "HIGH SCORE:{:,}".format(high_score)
		self.high_score_image = self.font.render(high_score_str, True, 
			self.text_color, self.aa_settings.bckg_color)
			
		#positions the image of high score:
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = self.score_rect.top
		
	def prep_level(self):
		"""level is displayed as image"""
		lvl = int(round(self.stats.level))
		lvl_str =  "LEVEL:{:,}".format(lvl)
		self.level_image = self.font.render(lvl_str, True,
			self.text_color, self.aa_settings.bckg_color)
			
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.score_rect.right
		self.level_rect.top =  self.score_rect.bottom + 10
		
		
		
	def prep_ships(self):
		"""indicates no of ships left"""
		self.ships = Group()
		for ship_i in range(self.stats.ship_left):
			ship = Ship(self.aa_settings,self.screen)
			ship.rect.x = 10 + ship_i * ship.rect.width
			ship.rect.y = 10
			self.ships.add(ship)
			
		
	def show_score(self):
		"""blits the scoreboard to screen"""
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.high_score_image, self.high_score_rect)
		self.screen.blit(self.level_image, self.level_rect)
		self.ships.draw(self.screen)
		

	
