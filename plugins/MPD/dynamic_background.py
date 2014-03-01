import random



class DynamicBackground (object):
    instance = None       
    def __new__(cls, *args, **kargs): 
        if cls.instance is None:
            cls.instance = object.__new__(cls, *args, **kargs)
    	    #Set background colors
	    cls.instance.colorR = random.randint(0, 255)
	    cls.instance.colorG = random.randint(0, 255)
	    cls.instance.colorB = random.randint(0, 255)
	    cls.instance.setNewColor()
           
        return cls.instance



    #changes the color of the background	
    def fillDynamicBackgroundColor(self,surface):
	if self.colorR < self.R:
		self.colorR=self.colorR+1
	if self.colorR>self.R:
		self.colorR=self.colorR-1
	if self.colorG < self.G:
		self.colorG=self.colorG+1
	if self.colorG>self.G:
		self.colorG=self.colorG-1
	if self.colorB < self.B:
		self.colorB=self.colorB+1
	if self.colorB>self.B:
		self.colorB=self.colorB-1
	#if we are in the desired color set a new target color
	if self.colorR==self.R and self.colorG==self.G and self.colorB==self.B:
		self.setNewColor()
	surface.fill([self.colorR,self.colorG,self.colorB])

    #set new target color
    def setNewColor(self):
	self.R = random.randint(0, 255)
	self.G = random.randint(0, 255)
	self.B = random.randint(0, 255)
	if (self.R+self.G+self.B) > 500:
		self.setNewColor()


