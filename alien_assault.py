#uses alien_assault_settings as instance here, so modify
import sys
import pygame
from alien_assault_settings import Settings
from ship import Ship
from aa_stats import aa_stats
from buttons import Button
from scores import scores
from game_functions import Check_events, Update_screen, update_bullets, create_aliens,update_aliens
from pygame.sprite import Group


def initiate_game():
	'''set up game unto screen'''
	pygame.init() #initialises background settings that pygame need to work with
	aa_settings = Settings() 
	screen = pygame.display.set_mode((aa_settings.screen_width, aa_settings.screen_height))
	pygame.display.set_caption('ALIEN ASSAULT')
   
	#draws the ship to screen:
	ship = Ship(aa_settings, screen)#make an instance first
	bullets = Group()#makes a group of bullets(instance)
	aliens = Group()#make a group of aliens(instance)
	#instance of alien:
	create_aliens(aa_settings, screen, ship, aliens)
	
	#create an instance of game_stats:
	stats = aa_stats(aa_settings)
	
	#create an instance of scoreboard
	show_scores = scores(aa_settings,screen,stats)
	
	#displays play button
	play_button = Button(aa_settings,screen,"Play")

#this  starts the main loop for the game
	while True:
		#observe keyboard and mouse events:
		Check_events(aa_settings,screen,stats,show_scores,
			play_button,ship, aliens, bullets)
		if stats.game_active:
			ship.update()
			update_bullets(aa_settings, screen,stats,
				show_scores, ship, aliens,bullets)
			update_aliens(aa_settings,screen,stats,show_scores,
				ship,aliens, bullets)
		Update_screen(aa_settings, screen,stats, show_scores, ship,
			aliens, bullets,play_button)
				
initiate_game()

