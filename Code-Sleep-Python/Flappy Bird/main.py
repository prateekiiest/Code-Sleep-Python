import pygame
import random

from objects import Grumpy, Pipe, Base, Score

# Setup *******************************************

pygame.init()
SCREEN = WIDTH, HEIGHT = 288, 512
display_height = 0.80 * HEIGHT
info = pygame.display.Info()

width = info.current_w
height = info.current_h

if width >= height:
	win = pygame.display.set_mode(SCREEN, pygame.NOFRAME)
else:
	win = pygame.display.set_mode(SCREEN, pygame.NOFRAME | pygame.SCALED | pygame.FULLSCREEN)

# win = pygame.display.set_mode(SCREEN, pygame.SCALED | pygame.FULLSCREEN)
clock = pygame.time.Clock()
FPS = 60

# COLORS

RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Backgrounds

bg1 = pygame.image.load('Assets/background-day.png')
bg2 = pygame.image.load('Assets/background-night.png')

bg = random.choice([bg1, bg2])

im_list = [pygame.image.load('Assets/pipe-green.png'), pygame.image.load('Assets/pipe-red.png')]
pipe_img = random.choice(im_list)

gameover_img =  pygame.image.load('Assets/gameover.png')
flappybird_img =  pygame.image.load('Assets/flappybird.png')
flappybird_img = pygame.transform.scale(flappybird_img, (200,80))

# Sounds & fx


die_fx = pygame.mixer.Sound('Sounds/die.wav')
hit_fx = pygame.mixer.Sound('Sounds/hit.wav')
point_fx = pygame.mixer.Sound('Sounds/point.wav')
swoosh_fx = pygame.mixer.Sound('Sounds/swoosh.wav')
wing_fx = pygame.mixer.Sound('Sounds/wing.wav')

# Objects

pipe_group = pygame.sprite.Group()
base = Base(win)
score_img = Score(WIDTH // 2, 50, win)
grumpy = Grumpy(win)

# Variables

base_height = 0.80 * HEIGHT
speed = 0
game_started = False
game_over = False
restart = False
score = 0
start_screen = True
pipe_pass = False
pipe_frequency = 1600

running =  True
while running:
	win.blit(bg, (0,0))
	
	if start_screen:
		speed = 0
		grumpy.draw_flap()
		base.update(speed)
		
		win.blit(flappybird_img, (40, 50))
	else:
		
		if game_started and not game_over:
			
			next_pipe = pygame.time.get_ticks()
			if next_pipe - last_pipe >= pipe_frequency:
				y = display_height // 2
				pipe_pos = random.choice(range(-100,100,4))
				height = y + pipe_pos
				
				top = Pipe(win, pipe_img, height, 1)
				bottom = Pipe(win, pipe_img, height, -1)
				pipe_group.add(top)
				pipe_group.add(bottom)
				last_pipe = next_pipe
		
		pipe_group.update(speed)
		base.update(speed)	
		grumpy.update()
		score_img.update(score)
		
		if pygame.sprite.spritecollide(grumpy, pipe_group, False) or grumpy.rect.top <= 0:
			game_started = False
			if grumpy.alive:
				hit_fx.play()
				die_fx.play()
			grumpy.alive = False
			grumpy.theta = grumpy.vel * -2
	
		if grumpy.rect.bottom >= display_height:
			speed = 0
			game_over = True
	
		if len(pipe_group) > 0:
			p = pipe_group.sprites()[0]
			if grumpy.rect.left > p.rect.left and grumpy.rect.right < p.rect.right and not pipe_pass and grumpy.alive:
				pipe_pass = True
	
			if pipe_pass:
				if grumpy.rect.left > p.rect.right:
					pipe_pass = False
					score += 1
					point_fx.play()
					
	if not grumpy.alive:
		win.blit(gameover_img, (50,200))
		
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE or \
				event.key == pygame.K_q:
				running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if start_screen:
				game_started = True
				speed = 2
				start_screen = False

				game_over = False
			#	grumpy.reset()
				last_pipe = pygame.time.get_ticks() - pipe_frequency
				next_pipe = 0
				pipe_group.empty()
				
				speed = 2
				score = 0
				
			if game_over:
				start_screen = True
				grumpy = Grumpy(win)
				pipe_img = random.choice(im_list)
				bg = random.choice([bg1, bg2])
				
			

	clock.tick(FPS)
	pygame.display.update()
pygame.quit()