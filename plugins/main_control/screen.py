from displayscreen import PiInfoScreen
import subprocess
import random

class myScreen(PiInfoScreen):
    refreshtime = 30
    displaytime = 5
    pluginname = "Main Control"
    plugininfo = "Shutdown, restart or exit"
    
    def setPluginVariables(self):
	self.myfont = pygame.font.SysFont("freesans", 50)
	self.touch = {'SHUTDOWN':None,'RESET':None}
        
    def showScreen(self):
	y=0
	color=self.randomColor()
	negativeColor=[255-color[0],255-color[1],255-color[2]]
        self.surface.fill(color)
        shutdownLabel = self.myfont.render("Shutdown", 1, negativeColor)
	self.touch['SHUTDOWN']=pygame.Rect((0,y),shutdownLabel.get_size())
	self.surface.blit(shutdownLabel, (0,0))
	y=y+shutdownLabel.get_height()
	resetLabel = self.myfont.render("Restart", 1, negativeColor)
	self.touch['RESET']=pygame.Rect((0,y),resetLabel.get_size())
	self.surface.blit(resetLabel, (0,y))
       

        # Scale our surface to the required screensize before sending back
        scaled = pygame.transform.scale(self.surface,self.screensize)
        self.screen.blit(scaled,(0,0))

        return self.screen

    def randomColor(self):
	color = []
	for i in {0,1,2}:
		color.append(random.randint(0,255))
	return color
	

    def mouseReleased(self, swipe, pos):
	if swipe == 0:
		for touch_elem in self.touch:
			if self.touch[touch_elem].collidepoint(pos):
				self.elemTouched(touch_elem)

    def elemTouched(self, elem):
	if elem=='SHUTDOWN':
		p=subprocess.Popen("shutdown now", stdout=subprocess.PIPE,shell=True)
		output, err = p.communicate()
	elif elem=='RESET':
		p=subprocess.Popen("shutdown -r now",stdout=subprocess.PIPE, shell=True)
		output, err = p.communicate()
