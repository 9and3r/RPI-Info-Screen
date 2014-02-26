import os
from time import strftime
from displayscreen import PiInfoScreen
import pygame

class myScreen(PiInfoScreen):
    refreshtime = 1
    displaytime = 10
    pluginname = "Clock"
    plugininfo = "Basic digital clock"
    
    def setPluginVariables(self):
        self.clockfont = os.path.join(self.plugindir, "resources", "SFDigitalReadout-Medium.ttf")         
        self.myfont = pygame.font.Font(self.clockfont, 100)
        
    def showScreen(self):
        self.surface.fill([0,0,0])
        mytime = strftime("%H:%M:%S")
        clocklabel = self.myfont.render(mytime, 1, [255,255,255])
        textpos = clocklabel.get_rect()
        textpos.centery = self.surface.get_rect().centery
        self.surface.blit(clocklabel, textpos) 

        # Scale our surface to the required screensize before sending back
        scaled = pygame.transform.scale(self.surface,self.screensize)
        self.screen.blit(scaled,(0,0))

        return self.screen
