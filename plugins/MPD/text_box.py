import pygame
class Text_Box:
	def __init__(self, text, x,y,width,surface,font):
		self.x = x
		self.y = y
		self.originalText = text
		self.text = text
		self.width = width
		self.surface = surface
		self.font = font
		self.timeLast = 0
		self.readyText = None
		self.canFit()
		
		
	def canFit(self):
		self.readyText = self.font.render(self.text, 1, [255,255,255])
		if self.width == -1:
			if self.surface.get_rect().width < self.x +self.readyText.get_rect().width:
				self.fit = False
				self.text = self.text + '      '
			else:
				self.fit = True

		else:
			if self.x + self.width < self.x +self.readyText.get_rect().width:
				self.fit = False
				self.text = self.text + '      '
			else:
				self.fit = True
		self.readyText

	def printInSurfaceText(self):
		if not self.fit:
			var = self.text[0]
			self.text = self.text[1:(len(self.text))] + var
			self.timeLast = 0
			self.readyText = self.font.render(self.text, 1, [255,255,255])
		self.surface.blit(self.readyText, (self.x, self.y))

	def getReadyText(self):
		return self.readyText
