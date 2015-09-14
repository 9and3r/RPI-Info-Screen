from displayscreen import PiInfoScreen
import subprocess
import pygame
import mpd
import os
import thread
import logging
import time
import math
import sys
import pygame
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from mpd_client import MPD
from dynamic_background import DynamicBackground
from song_view import Song_View
from playlist_view import Playlist_View

class myScreen(PiInfoScreen):
    refreshtime = 0.1
    displaytime = 5
    pluginname = "MPD Control"
    plugininfo = "Control your MPD server"
    
    def setPluginVariables(self):
	#Load variables
	fanart_key = "REPLACE WITH API KEY FROM https://fanart.tv/get-an-api-key/"
	# Connect to MDP server
	self.ip = 'localhost'
	self.port = '6600'
	logging.basicConfig()
	self.client = mpd.MPDClient()
	self.connected = False
	thread.start_new_thread(self.connectMDPserver,())
	self.screens = []
	self.screens.append(MPD(self.client,fanart_key))
	self.screens.append(Playlist_View(self.client,self))
	self.screens.append(Song_View(self.client))
	self.currentScreen = 0

    def showScreen(self):
	if self.connected:
		self.surface = self.screens[self.currentScreen].showScreen(self.surface)
	else:
		self.surface = self.showNotConnected()

	# Scale our surface to the required screensize before sending back
        scaled = pygame.transform.scale(self.surface,self.screensize)
        self.screen.blit(scaled,(0,0))

    def connectMDPserver(self):
	# Connect to MDP server
	try:
		self.client.connect(self.ip, self.port)
		self.connected = True
			
	except:
		self.connected = False
		time.sleep(10)
		self.connectMDPserver()

    def showNotConnected(self):
	DynamicBackground().fillDynamicBackgroundColor(self.surface)
	myfont = pygame.font.SysFont(None, 30)
	nowtext = myfont.render("Could not connect to MPD server", 1, (255,255,255))
        self.surface.blit(nowtext, (0, 0))
	nowtext = myfont.render("Check the configuration", 1, (255,255,255))
        self.surface.blit(nowtext, (0, 50))
	nowtext = myfont.render("Anyway the software is trying to connect", 1, (255,255,255))
        self.surface.blit(nowtext, (0, 100))
	return self.surface
    
    def changeScreen(self):
	self.currentScreen= self.currentScreen +1
	if self.currentScreen >1:
		self.currentScreen = 0

    def mouseReleased(self, swipe, posDown,posUp ,longPress):
	if(swipe>2):
		self.screens[self.currentScreen].swipe(swipe)
	elif swipe==2:
		self.changeScreen()
	else:
		self.screens[self.currentScreen].mouseClick(posDown, posUp,longPress)

    def changeToPlaylist(self, playlist):
	self.screens[2].setPlaylist(playlist, self.surface)
	self.currentScreen = 2
	


