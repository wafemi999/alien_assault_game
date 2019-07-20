import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	
	
	def __init__(self, aa_settings, screen):
		'''initialises the ship and set to center position'''
		super(Ship, self).__init__()
		self.screen = screen
		self.aa_settings = aa_settings
		#load image and get rect:
		self.image = pygame.image.load('images/ship_2.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		#placing the ship at the bottom_center of the screen:
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		#stores a decimal value forthe ship's center:
		self.center = float(self.rect.centerx)
		
		#stops movement(continuos flag)
		self.moving_right = False
		self.moving_left = False
		
	def update(self):
		'''updates shipping position based on movement flag'''
		#update ships center value, not rect
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.aa_settings.ship_speed_factor 
		if self.moving_left and self.rect.left > 0:
			self.center -= self.aa_settings.ship_speed_factor 
			
		#update rect from self.center
		self.rect.centerx = self.center
		
	def blitme(self):
		'''draws the ship at center of screen'''
		self.screen.blit(self.image, self.rect)
	
	def center_ship(self):
		"""re-centers the position of the ship"""
		self.center = self.screen_rect.centerx
		
