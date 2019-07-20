import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	'''A class containing aliens'''
	def __init__(self,aa_settings, screen):
		'''set atrributes and methods for alien'''
		super(Alien,self).__init__()
		self.screen = screen
		self.aa_settings = aa_settings
		
		#load image and position attribute
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()
		
		#positioning the alien
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		
		# alien position
		self.x = float(self.rect.x)
		
	def blitme(self):
		'''drawing the alien to screen'''
		self.screen.blit(self.image, self.rect)
		
		
	def check_edges(self):
		''' this checks if the alien hit the screen edge'''
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <=0:
			return True
		
	def update(self):
		'''moves aliens to the right or left'''
		self.x += (self.aa_settings.alien_speed_factor * 
			self.aa_settings.aliens_direction)
		self.rect.x = self.x
		
	
	
