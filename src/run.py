import pygame
from pygame.locals import *
from constants import constants
from pacman import Pacman


class GameController(object):
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode(constants.SCREENSIZE.value, 0, 32)
		self.background = None
		self.clock = pygame.time.Clock()
		self.pacman = Pacman()

	def setBackground(self):
		self.background = pygame.surface.Surface(constants.SCREENSIZE.value).convert()
		self.background.fill(constants.BLACK.value)

	def startGame(self):
		self.setBackground()

	def update(self):
		dt = self.clock.tick(30) / 1000.0
		self.pacman.update(dt)
		self.checkEvents()
		self.render()

	def checkEvents(self):
		for event in pygame.event.get():
			if event.type == QUIT:
				exit()

	def render(self):
		self.screen.blit(self.background, (0, 0))
		self.pacman.render(self.screen)
		pygame.display.update()


if __name__ == "__main__":
	game = GameController()
	game.startGame()
	while True:
		game.update()
