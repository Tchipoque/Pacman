import pygame
from vector import Vector2
from constants import constants


class Node():
	def __init__(self, x, y):
		self.position = Vector2(x, y)
		self.neighbors = {constants.UP.value : None, constants.DOWN.value: None, constants.LEFT.value: None, constants.RIGHT.value: None}

	def render(self, screen):
		for n in self.neighbors.keys():
			if self.neighbors[n] is not None:
				line_start = self.position.asTuple()
				line_end = self.neighbors[n].position.asTuple()
				pygame.draw.line(screen, constants.WHITE.value, line_start, line_end, 4)
				pygame.draw.circle(screen, constants.RED.value, self.position.asInt(), 12)


class NodeGroup():
	def __init__(self):
		self.nodeList = []

	def setupTestNodes(self):
		nodeA = Node(80 ,80)
		nodeB = Node(160, 80)
		nodeC = Node(80, 160)
		nodeD = Node(160, 160)
		nodeE = Node(208, 160)
		nodeF = Node(80, 320)
		nodeG = Node(208, 320)
		nodeA.neighbors[constants.RIGHT.value] = nodeB
		nodeA.neighbors[constants.DOWN.value] = nodeC
		nodeB.neighbors[constants.LEFT.value] = nodeA
		nodeB.neighbors[constants.DOWN.value] = nodeD
		nodeC.neighbors[constants.UP.value] = nodeA
		nodeC.neighbors[constants.RIGHT.value] = nodeD
		nodeC.neighbors[constants.DOWN.value] = nodeF
		nodeD.neighbors[constants.UP.value] = nodeB
		nodeD.neighbors[constants.LEFT.value] = nodeC
		nodeD.neighbors[constants.RIGHT.value] = nodeE
		nodeE.neighbors[constants.LEFT.value] = nodeD
		nodeE.neighbors[constants.DOWN.value] = nodeG
		nodeF.neighbors[constants.UP.value] = nodeC
		nodeF.neighbors[constants.RIGHT.value] = nodeG
		nodeG.neighbors[constants.UP.value] = nodeE
		nodeG.neighbors[constants.LEFT.value] = nodeF
		self.nodeList = [nodeA, nodeB, nodeC, nodeD, nodeE, nodeF, nodeG]

	def render(self, screen):
		for node in self.nodeList:
			node.render(screen)
