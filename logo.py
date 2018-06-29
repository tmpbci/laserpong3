# coding=UTF-8
'''

@author: Sam Neurohack

'''

import vectors
import gstt

LOGO = [
	# L/o
	[[(-140,-100),(-200,20),(40,20)],0xFF00],
	# aser
	[[(-140,-40),(-100,-40,),(-120,0),(-160,0),(-110,-20)],0xFFFF],
	[[(-40,-40),(-60,-40),(-90,-20),(-50,-20),(-80,0),(-100,0)],0xFFFF],
	[[(-30,-20),(10,-20),(0,-40),(-20,-40),(-30,-20),(-30,0),(-10,0)],0xFFFF],
	[[(20,0),(40,-40),(35,-30),(50,-40),(70,-40)],0xFFFF],
	# Pinball
	[[(-185,50),(-145,50),(-130,20),(-170,20),(-200,80)],0xFFFF00],  	#P
	[[(-80,40),(-120,40),(-140,80),(-100,80),(-80,40)],0xFFFF],			#O
	[[(-80,80),(-60,40),(-65,50),(-40,40),(-25,50),(-40,80)],0xFFFF],	#N
	[[(40,40),(0,40),(-20,80),(20,80),(30,60),(10,60)],0xFFFF],		#G
	]

#LOGO_OFFSET = vectors.Vector2D(200,-100)
LOGO_OFFSET = vectors.Vector2D(460,250)

def Draw(f):
	'''
	Dessine le logo
	'''
	for pl_color in LOGO:
		c = pl_color[1]
		xy_list = []
		for xy in pl_color[0]:
			xy_list.append((LOGO_OFFSET + vectors.Vector2D(xy[0],xy[1])).ToTuple())
		#print xy_list
		f.PolyLineOneColor(xy_list, c)



