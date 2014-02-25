from displayscreen import PiInfoScreen

class myScreen(PiInfoScreen):
    refreshtime = 30
    displaytime = 5
    pluginname = "Main Control"
    plugininfo = "Shutdown, restart or exit"
    
    def setPluginVariables(self):
	self.myfont = pygame.font.SysFont("freesans", 50)
	self.touch = {'SHUTDOWN':None,'RESTART':None,'EXIT':None}
        
    def showScreen(self):
        self.surface.fill([14,167,255])
        label = self.myfont.render("Shutdown", 1, [255,255,255])
	self.touch['SHUTDOWN']=pygame.Rect((0,0),label.get_size())
	self.touch['EXIT']=pygame.Rect((0,0),label.get_size())
	self.touch['RESTART']=pygame.Rect((0,0),label.get_size())
        self.surface.blit(label, (0,0))

        # Scale our surface to the required screensize before sending back
        scaled = pygame.transform.scale(self.surface,self.screensize)
        self.screen.blit(scaled,(0,0))

        return self.screen

    def mouseReleased(self, swipe, pos):
	if swipe == 0:
		for touch_elem in self.touch:
			print touch_elem
			if self.touch[touch_elem].collidepoint(pos):
				self.elemTouched(touch_elem)

    def elemTouched(self, elem):
	if elem=='SHUTDOWN':
		print "shutdown"
