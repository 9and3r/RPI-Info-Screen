RPI-Info-Screen
===============

To use the MPD plugin you need some libraries:

https://github.com/z4r/python-fanart
https://musicbrainz.org/doc/python-musicbrainz2
https://github.com/Mic92/python-mpd2

See http://www.raspberrypi.org/phpBB3/viewtopic.php?f=41&amp;t=51807

BETA VERSION - EXPECT ERRORS!

Before running:  
1) Remove the plugin folders you don't want to use (I haven't got round to implementing a way of enabling/disabing plugins yet).  
2) Edit default.py - Line 16 sets the screen size (this will be moved into a config file at some point)  
3) Run default.py  
4) Pressing "n" moves between screens, "q" quits (this should be handled by GPIO at a later date)  

Any problems, you can post issues on GitHub and I may take a look!

To Do
-----

[ ] Use FPS limiting to reduce cycles on Pi


