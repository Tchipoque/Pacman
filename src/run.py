import pygame
from pygame.locals import *
from constants import constants


class GameController(object):
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode(constants.SCREENSIZE.value, 0, 32)
		self.background = None

	def setBackground(self):
		self.background = pygame.surface.Surface(constants.SCREENSIZE.value).convert()
		self.background.fill(constants.BLACK.value)

	def startGame(self):
		self.setBackground()

	def update(self):
		self.checkEvents()
		self.render()

	def checkEvents(self):
		for event in pygame.event.get():
			if event.type == QUIT:
				exit()

	def render(self):
		pygame.display.update()


if __name__ == "__main__":
	game = GameController()
	game.startGame()
	while True:
		game.update()
