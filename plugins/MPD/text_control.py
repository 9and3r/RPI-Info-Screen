import pygame
from text_box import Text_Box



class Text_Control(object):

   instance = None       
   def __new__(cls, *args, **kargs): 
        if cls.instance is None:
            	cls.instance = object.__new__(cls, *args, **kargs)
		cls.instance.strings = {}
  	return cls.instance


   def changeText(self,key, text, x, y, width,surface,font):
	self.strings.update({key : Text_Box(text, x, y, width, surface, font)})
	return self.strings[key].getReadyText()

   def printKey(self,key):
	self.strings[key].printInSurfaceText()


