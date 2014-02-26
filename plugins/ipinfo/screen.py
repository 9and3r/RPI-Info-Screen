import subprocess
import pygame
from displayscreen import PiInfoScreen

class myScreen(PiInfoScreen):
    refreshtime = 30
    displaytime = 5
    pluginname = "IP info"
    plugininfo = "Shows the IP address"
    
    def setPluginVariables(self):
	self.myfont = pygame.font.SysFont("freesans", 30)
        
    def showScreen(self):
	# Call ifconfig and store in a string
	ifconfig = subprocess.Popen("ifconfig", stdout=subprocess.PIPE, shell=True)
	output, err = ifconfig.communicate()
	# Proces the string
	ipList = {}
	lines=output.split('\n')
	i=0
	while i <len(lines):
		if lines[i].find("eth")!=-1 or lines[i].find("wlan")!=-1:
			interface = lines[i].split(" ")[0]
			i=i+1
			ip = lines[i].split(":")[1].split(" ")[0]
			if ip.find(".")==-1:
				ipList.update({interface:"Not connected"})
			else:
				ipList.update({interface:ip})
		i=i+1
			
	
        self.surface.fill([14,167,255])
	y=0
	for ip in ipList:
		label = self.myfont.render(ip+": "+ipList[ip], 1, [255,255,255])
        	self.surface.blit(label, (0,y))
		y = y + label.get_height()
        
        # Scale our surface to the required screensize before sending back
        scaled = pygame.transform.scale(self.surface,self.screensize)
        self.screen.blit(scaled,(0,0))

        return self.screen


