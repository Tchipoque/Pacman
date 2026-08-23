import pygame
from pygame.locals import *
from vector import Vector2
from constants import constants


class Pacman():
	def __init__(self):
		self.name = constants.PACMAN.value
		self.position = Vector2(200, 400)
		self.directions = {constants.STOP.value: Vector2(), constants.UP.value : Vector2(0, -1), constants.DOWN.value: Vector2(0, 1), constants.LEFT.value: Vector2(-1, 0), constants.RIGHT.value: Vector2(1, 0)}
		self.direction = constants.STOP.value
		self.speed = 100 * constants.TILEWIDTH.value/16
		self.radius = 10
		self.color = constants.YELLOW.value

	def update(self, dt):
		self.position += self.directions[self.direction] * self.speed * dt
		direction = self.getValidKey()
		self.direction = direction

	def getValidKey(self):
		key_pressed = pygame.key.get_pressed()
		if key_pressed[K_UP]:
			return constants.UP.value
		if key_pressed[K_DOWN]:
			return constants.DOWN.value
		if key_pressed[K_LEFT]:
			return constants.LEFT.value
		if key_pressed[K_RIGHT]:
			return constants.RIGHT.value
		return constants.STOP.value

	def render(self, screen):
		p = self.position.asInt()
		pygame.draw.circle(screen, self.color, p, self.radius)
