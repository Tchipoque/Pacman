import pygame
from pygame.locals import *
from vector import Vector2
from constants import constants


class Pacman():
	def __init__(self, node):
		self.name = constants.PACMAN.value
		self.directions = {constants.STOP.value: Vector2(), constants.UP.value : Vector2(0, -1),
					  constants.DOWN.value: Vector2(0, 1), constants.LEFT.value: Vector2(-1, 0),
					   constants.RIGHT.value: Vector2(1, 0)}
		self.direction = constants.STOP.value
		self.speed = 100 * constants.TILEWIDTH.value/16
		self.radius = 10
		self.color = constants.YELLOW.value
		self.node = node
		self.setPosition()
		self.target = node

	def setPosition(self):
		self.position = self.node.position.copy()

	def update(self, dt):
		self.position += self.directions[self.direction] * self.speed * dt
		direction = self.getValidKey()
		if self.overshotTarget():
			self.node = self.target
			self.target = self.getNewTarget(direction)
			if self.target is not self.node:
				self.direction = direction
			else:
				self.target = self.getNewTarget(self.direction)

			if self.target is self.node:
				self.direction = constants.STOP.value
			self.setPosition()
		else:
			if self.oppositeDirection(direction):
				self.reverseDriection()

	def validDirection(self, direction):
		if direction is not constants.STOP.value:
			if self.node.neighbors[direction] is not None:
				return True
		return False

	def getNewTarget(self, direction):
		if self.validDirection(direction):
			return self.node.neighbors[direction]
		return self.node

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

	def overshotTarget(self):
		if self.target is not None:
			vec1 = self.target.position - self.node.position
			vec2 = self.position - self.node.position
			node2Target = vec1.magnitudeSquared()
			node2Self = vec2.magnitudeSquared()
			return node2Self >= node2Target
		return False

	def reverseDriection(self):
		self.direction *= -1
		temp = self.node
		self.node = self.target
		self.target = temp

	def oppositeDirection(self, direction):
		if direction is not constants.STOP.value:
			if direction == self.direction * -1:
				return True
		return False

