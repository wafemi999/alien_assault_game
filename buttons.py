import pygame.font
class Button:
	def __init__(self, aa_settings,screen,txt):
		"""button attributes"""
		self.screen = screen
		self.screen_rect = screen.get_rect()
	
	#create button dimensions
		self.width, self.height  = 100, 50
		self.button_color = (0,255,0)
		self.text_color = (255,255,255)
		self.font = pygame.font.SysFont(None,45)
	
		self.rect = pygame.Rect(0,0, self.width, self.height)
		self.rect.center = self.screen_rect.center
	
		self.call_txt(txt)
	
	
	def call_txt(self, txt):
		"""turns text into image"""
		self.txt_img = self.font.render(txt,True,self.button_color,
			self.text_color, )
			
		self.txt_img_rect = self.txt_img.get_rect()
		self.txt_img_rect.center = self.rect.center
		
		
	def draw_button(self):
		"""1:draw a blank button and 2:draw the text into it"""
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.txt_img, self.txt_img_rect)  
