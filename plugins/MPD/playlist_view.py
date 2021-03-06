import pygame
import mpd
from dynamic_background import DynamicBackground

class Playlist_View:

	def __init__(self,client,mpd_control):
		self.client=client
		self.currentPage = 0
		self.maxInView = 5
		self.control = mpd_control
		self.touchList = {}
		self.showPlaylist = []


 	def mouseClick(self, mouseDownPos, mouseUpPos, longPress):
		for key in self.touchList:
			if longPress:
				for i in range(0, self.maxInView):
					if key == ('PLAYLIST'+str(i)):
						if self.touchList[key].collidepoint(mouseDownPos) and self.touchList[key].collidepoint(mouseUpPos):
							self.control.changeToPlaylist(self.playlists[i]['playlist'])
			else:
				for i in range(0, self.maxInView):
					if key == ('PLAYLIST'+str(i)):
						if self.touchList[key].collidepoint(mouseDownPos) and self.touchList[key].collidepoint(mouseUpPos):
							self.control.changeToPlaylist(self.playlists[i]['playlist'])

	def changePlayList(self, i):
		self.client.clear()
		self.client.load(self.playlists[i]['playlist'])
		if self.client.status()['state'] != 'play':
			self.client.play()

	def getMax(self):
		if len(self.playlists) > self.maxInView:
			return self.maxInView 
		else:
			return len(self.playlists)	
	

	def swipe(self,swipe):
		pass	

	def showScreen(self,surface):
		self.surface=surface
		self.showPlaylist = []
		DynamicBackground().fillDynamicBackgroundColor(self.surface)
		self.playlists = self.client.listplaylists()
		myfont = pygame.font.SysFont(None, 30)
		mainText = myfont.render('Playlists', 1, [255,255,255])
		self.surface.blit(mainText,(self.surface.get_width()/2-mainText.get_rect().width/2, 0))
		y = mainText.get_height()
		for i in range(0,self.getMax()):
			self.showPlaylist.append(myfont.render(self.playlists[i]['playlist'], 1, [255,255,255]))
        		self.surface.blit(self.showPlaylist[i],(0, y))
			# insert in the touch dictionary
			name = 'PLAYLIST'+str(i)
			value = pygame.Rect(0,y,self.showPlaylist[i].get_rect().width,self.showPlaylist[i].get_rect().height)
			self.touchList.update({name : value})
			y = y + self.showPlaylist[i].get_height()
		return self.surface
