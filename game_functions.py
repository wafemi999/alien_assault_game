import sys
from bullets import Bullets
import pygame
from alien import Alien
from time import sleep



def check_keydown_events(event, aa_settings, screen, ship, bullets):
	'''respond to keypresses'''
	
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key ==  pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		#creating new bullets and no of bullets allowed:
		fire_bullet(aa_settings,screen, ship, bullets)
		
	elif event.key == pygame.K_e:
		sys.exit()
	

def check_keyup_events(event, ship):
	'''responds to key releases'''
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key ==  pygame.K_LEFT:
		ship.moving_left = False 
	
	
	
def Check_events(aa_settings, screen , stats, show_score, play_button,
	ship, aliens, bullets ):
	'''responds to key_press and mouse events'''
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	#responds to keypressed event
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, aa_settings, screen, ship,
				bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(aa_settings, screen, stats, show_score,
				play_button, ship, aliens, bullets, mouse_x, mouse_y)
			
def check_play_button(aa_settings, screen, stats,show_score,play_button,
	ship, aliens, bullets, mouse_x,mouse_y):
	"""game runs when player clicks the play button"""
	button_clicked  = play_button.rect.collidepoint(mouse_x,mouse_y)
	if button_clicked and not stats.game_active:
		aa_settings.dynamic_settings()
		pygame.mouse.set_visible(False)
		stats.reset_stats()
		stats.game_active = True
		
		
		
	#reset the images on game window
	show_score.prep_score()
	show_score.prep_high_score()
	show_score.prep_level()
	show_score.prep_ships()
	
		
	# reset aliens and ship are redefined
	aliens.empty()
	bullets.empty()
	
	create_aliens(aa_settings,screen,ship,aliens)
	ship.center_ship()
	
	
				
def Update_screen(aa_settings,screen,stats, show_scores, ship, aliens, bullets,play_button):
	'''updates image in the screen and flips screes'''
	#redraws screen through every loop
	screen.fill(aa_settings.bckg_color)
	
	#displays the score info:
	show_scores.show_score()
	
	#this redraws the bullet behind the ship and aliens
	for bullet in bullets.sprites():
		bullet.draw_bullet ()
	ship.blitme()
	aliens.draw(screen)
	if not stats.game_active:
		play_button.draw_button()	
	#this makes the recently drawn objects  visible:
	pygame.display.flip()



def update_bullets(aa_settings,screen,stats, show_score, ship,aliens,bullets):
		'''updates bullets and delets old bullets'''
		bullets.update()
		#get rid of bullets that have dissappeard.
		for bullet in bullets.copy():
			if bullet.rect.bottom <= 0:
				bullets.remove(bullet)#print(len(bullets))#test
		
		#check if there is an alien_bullet collision
		alien_bullet_collisions(aa_settings,screen,stats,
			show_score, ship,aliens,bullets)
		
def check_high_score(stats, show_score):
	'''confirms the high score'''
	if stats.score > stats.high_score:
		stats.high_score = stats.score
		show_score.prep_high_score()
		
def alien_bullet_collisions(aa_settings,screen,stats, show_score,
	ship,aliens,bullets):
	"check if bullet collides with alien then deletes them:"
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
	if len(aliens) == 0:
		#destroy previous bullets
		bullets.empty()
		#create new set of aliens:
		aa_settings.increase_speed()
		
		#increase level:
		stats.level += 1
		show_score.prep_level()
		create_aliens(aa_settings,screen,ship,aliens)
		
	if collisions:
		for aliens in collisions.values():
			stats.score += aa_settings.alien_points * len(aliens)
			show_score.prep_score()
		check_high_score(stats,show_score)
		
		

		
def fire_bullet(aa_settings,screen, ship, bullets):
	''' handles firing of bullets'''
	if len(bullets) < aa_settings.bullet_allowed:
		new_bullet = Bullets(aa_settings, screen,ship)
		bullets.add(new_bullet)
		
		
		
		
def get_no_aliens(aa_settings, alien_width):
	'''determine the number of aliens tha will fit screen row'''
	available_x_space = aa_settings.screen_width - 2 * alien_width
	number_x_aliens = int(available_x_space / (2 * alien_width))
	return number_x_aliens
	
def get_no_of_rows(aa_settings, ship_height, alien_height):
	'''gives the exact no of rows aliens that will fit the screen perfectly '''
	available_y_space = (aa_settings.screen_height - (3 * alien_height) - ship_height)
	number_of_rows = int(available_y_space / (2 * alien_height) )
	return  number_of_rows	

def create_alien(aa_settings,screen,aliens, alien_no, row_number ):
	'''creates an alien and add to aliensGroup'''
	alien = Alien(aa_settings, screen )
	alien_width = alien.rect.width
	alien.x = alien_width + 2 * alien_width * alien_no
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number 
	aliens.add(alien)   
	
	
	
	
def create_aliens(aa_settings,screen,ship,aliens):
	'''this creates a  fleet of aliens'''
	#fits aliens into a row
	alien = Alien(aa_settings, screen)
	number_x_aliens = get_no_aliens(aa_settings, alien.rect.width)
	number_of_rows = get_no_of_rows(aa_settings, ship.rect.height,
		alien.rect.height)
		
	#creating a row of aliens
	for row_number in range(number_of_rows):
		for alien_no in range(number_x_aliens):
			create_alien(aa_settings,screen, aliens, alien_no, row_number)
			
			
def check_aliens_edges(aa_settings,aliens):
		'''responds when the aliens reach an edge'''
		for alien in aliens.sprites():
			if alien.check_edges():
				change_aliens_direction(aa_settings, aliens)
				break
				
def change_aliens_direction(aa_settings,aliens):
	"""this drops the ships and changes their directiom"""
	for alien in aliens.sprites():
		alien.rect.y += aa_settings.aliens_drop_speed
	aa_settings.aliens_direction *= -1
			

def ship_hit(aa_settings, screen,stats,show_score,ship,aliens,bullets):
	"""decreases ship limit when hit by alien"""
	if stats.ship_left > 0:
		stats.ship_left -= 1 
		show_score.prep_ships()
	
	#deletes list of aliens and bullets
		aliens.empty()
		bullets.empty()
		
		create_aliens(aa_settings,screen,ship,aliens)
		ship.center_ship()
		sleep(0.5)
	else:
		stats.game_active = False
		pygame.mouse.set_visible(True)
	
def aliens_reach_bottom(aa_settings,screen,stats,show_score,ship,aliens,
	bullets):
	"""confirms when n aliens hits the bottom of the screen"""
	screen_rect =  screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			ship_hit(aa_settings,screen,stats,show_score,ship,aliens,
				bullets)
			break
	
				

def update_aliens(aa_settings,stats,show_score,screen,ship,aliens,
	bullets):
	"checks if the aliens hit the screen edges and then update their direction"
	check_aliens_edges(aa_settings,aliens)
	
	'''moves all aliens at once'''
	aliens.update()
	#check for alien-ship collisions
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(aa_settings,stats,show_score,screen,ship,aliens,bullets)
	
	#check for aliens that hits screen bottom
	aliens_reach_bottom(aa_settings,stats, show_score,screen,ship,aliens,bullets)
	
		
		

	
	
	
	

	
	
		
		

	 
