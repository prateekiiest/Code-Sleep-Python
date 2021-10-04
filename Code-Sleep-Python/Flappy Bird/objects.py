import pygame
import random

SCREEN = WIDTH, HEIGHT = 288, 512
display_height = 0.80 * HEIGHT

pygame.mixer.init()
wing_fx = pygame.mixer.Sound('Sounds/wing.wav')

class Grumpy:
	def __init__(self, win):
		self.win = win

		self.im_list = []
		bird_color = random.choice(['red', 'blue', 'yellow'])
		for i in range(1,4):
			img =  pygame.image.load(f'Assets/Grumpy/{bird_color}{i}.png')
			self.im_list.append(img)
		
		self.reset()
		
	def update(self):
		# gravity
		self.vel += 0.3
		if self.vel >= 8:
			self.vel = 8
		if self.rect.bottom <= display_height:
			self.rect.y += int(self.vel)
		
		if self.alive:
			
			# jump
			if pygame.mouse.get_pressed()[0] == 1 and not self.jumped:
				wing_fx.play()
				self.jumped = True
				self.vel = -6
			if pygame.mouse.get_pressed()[0] == 0:
				self.jumped = False
			
			self.flap_counter()
			
			self.image = pygame.transform.rotate(self.im_list[self.index], self.vel * -2)
		else:
			if self.rect.bottom <= display_height:
				self.theta -= 2
			self.image = pygame.transform.rotate(self.im_list[self.index], self.theta)
			
	#	if not alive:
	#		self.image = self.im_list[1]
		
		self.win.blit(self.image, self.rect)
		
	def flap_counter(self):
		#animation
		self.counter += 1
		if self.counter > 5:
			self.counter = 0
			self.index += 1
		if self.index >= 3:
			self.index = 0
			
	def draw_flap(self):
		self.flap_counter()
		if self.flap_pos <= -10 or self.flap_pos > 10:
			self.flap_inc *= -1
		self.flap_pos += self.flap_inc
		self.rect.y += self.flap_inc
		self.rect.x = WIDTH // 2 - 20
		self.image = self.im_list[self.index]
		self.win.blit(self.image, self.rect)
		
	def reset(self):
		self.index = 0
		self.image = self.im_list[self.index]
		self.rect = self.image.get_rect()
		self.rect.x = 60
		self.rect.y = int(display_height) // 2
		self.counter = 0
		self.vel = 0
		self.jumped = False
		self.alive = True
		self.theta = 0
		self.mid_pos = display_height // 2
		self.flap_pos = 0
		self.flap_inc = 1

class Base:
	def __init__(self, win):
		self.win = win

		self.image1 = pygame.image.load('Assets/base.png')
		self.image2 = self.image1
		self.rect1 = self.image1.get_rect()
		self.rect1.x = 0
		self.rect1.y = int(display_height)
		self.rect2 = self.image2.get_rect()
		self.rect2.x = WIDTH
		self.rect2.y = int(display_height)
		
	def update(self, speed):
		self.rect1.x -= speed
		self.rect2.x -= speed
		
		if self.rect1.right <= 0:
			self.rect1.x = WIDTH - 5
		if self.rect2.right <= 0:
			self.rect2.x = WIDTH - 5

		self.win.blit(self.image1, self.rect1)
		self.win.blit(self.image2, self.rect2)


class Pipe(pygame.sprite.Sprite):
	def __init__(self, win, image, y, position):
		super(Pipe, self).__init__()
		
		self.win = win
		self.image = image
		self.rect = self.image.get_rect()
		pipe_gap = 100 // 2
		x = WIDTH

		if position == 1:
			self.image = pygame.transform.flip(self.image, False, True)
			self.rect.bottomleft = (x, y - pipe_gap)
		elif position == -1:
			self.rect.topleft = (x, y + pipe_gap)
		
	def update(self, speed):
		self.rect.x -= speed
		if self.rect.right < 0:
			self.kill()
		self.win.blit(self.image,  self.rect)
		
class Score:
	def __init__(self, x, y, win):
		self.score_list = []
		for score in range(10):
			img = pygame.image.load(f'Assets/Score/{score}.png')
			self.score_list.append(img)
			self.x = x
			self.y = y

		self.win = win
		
	def update(self, score):
		score = str(score)
		for index, num in enumerate(score):
			self.image = self.score_list[int(num)]
			self.rect = self.image.get_rect()
			self.rect.topleft = self.x - 15 * len(score) + 30 * index, self.y
			self.win.blit(self.image, self.rect)