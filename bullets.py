import pygame
from pygame.sprite import Sprite


class Bullets(Sprite):
	'''a class thats manage bullets fired by ship'''
	
	def __init__(self, aa_settings, screen,ship):
		'''this creates the bullet object'''
		super(Bullets, self).__init__()
		self.screen = screen
		#create a bullet at initial position (0,0)
		self.rect = pygame.Rect(0,0,aa_settings.bullet_width,
			aa_settings.bullet_height)
		self.rect.centerx  = ship.rect.centerx
		self.rect.top = ship.rect.top
		
		
		#store the bullets position as a decimal value:
		self.y = float(self.rect.y)
		self.speed_factor = aa_settings.bullets_speed_factor
		self.color = aa_settings.bullet_color
		
		
	def update(self):
		'''moves and update the bullet'''
		#position the bullet
		self.y -= self.speed_factor
		#updatethe rect position:
		self.rect.y = self.y            
		
	def draw_bullet(self):
		'''draws the bullet to screen'''
		pygame.draw.rect(self.screen, self.color,self.rect)
		
		
	
		
		
