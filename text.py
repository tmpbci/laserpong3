# coding=UTF-8
'''
Created on 25 janv. 2015

@author: pclf
'''

import gstt
import vectors
from globalVars import *


ZOOM_PLAYING = .5
ZOOM_GAMEOVER = 5.0
DZOOM_PLAYING = -.4
DZOOM_GAMEOVER = .1

# Finalement, on implémente le score ici
ASCII_GRAPHICS = [

#implementé

	[[(-10,10), (10,-10), (10,10), (0,20), (-10,10), (-10,-10), (0,-20), (10,-10)]],#0
	[[(-10,-10), (0,-20), (0,20)], [(-10,20), (10,20)]],							#1
	[[(-10,-10), (0,-20), (10,-10), (10,0), (-10,20), (10,20)]],					#2
	[[(-10,-20), (0,-20), (10,-10), (0,0), (10,10), (0,20), (-10,20)]],				#3
	[[(10,10), (-10,10), (0,-20), (0,20)]],											#4
	[[(10,-20), (-10,-20), (-10,0), (0,0), (10,10), (0,20), (-10,20)]],				#5
	[[(10,-20), (0,-20), (-10,-10), (-10,20), (0,20), (10,10), (10,0), (-10,0)]],	#6
	[[(-10,-20), (10,-20), (-10,20)]],												#7
	[[(-10,10), (10,-10), (0,-20), (-10,-10), (10,10), (0,20), (-10,10)]],			#8
	[[(10,0), (-10,0), (-10,-10), (0,-20), (10,-20), (10,10), (0,20), (-10,20)]],	#9

# A implementer	
	[[(-10,10), (10,-10), (10,10), (0,20), (-10,10), (-10,-10), (0,-20), (10,-10)]], #:
	[[(-10,-10), (0,-20), (0,20)], [(-10,20), (10,20)]],							#;
	[[(-10,-10), (0,-20), (10,-10), (10,0), (-10,20), (10,20)]],					#<
	[[(-10,-20), (0,-20), (10,-10), (0,0), (10,10), (0,20), (-10,20)]],				#=
	[[(10,10), (-10,10), (0,-20), (0,20)]],											#>
	[[(10,-20), (-10,-20), (-10,0), (0,0), (10,10), (0,20), (-10,20)]],				#?
	[[(10,-20), (0,-20), (-10,-10), (-10,20), (0,20), (10,10), (10,0), (-10,0)]],	#@

# Implementé
	
	[[(-10,20), (-10,-20), (10,-20), (10,20), (10,0), (-10,0)]],				#A
	[[(-10,20), (-10,-20), (10,-20), (10,20), (10,0), (-10,0)]],				#A
	[[(-10,20), (-10,-20), (10,-20), (10,20), (-10,20), (-10,0), (10,0)]],		#B
	[[(10,20), (-10,20), (-10,-20), (10,-20)]],									#C
	[[(-10,20), (-10,-20), (10,-20), (10,20), (-10,20)]],						#D
	[[(10,20), (-10,20), (-10,-0), (10,0), (-10,0), (-10,-20), (10,-20)]],		#E
	[[(-10,20), (-10,-0), (10,0), (-10,0), (-10,-20), (10,-20)]],				#F
	[[(0,0), (10,0), (10,20), (-10,20), (-10,-20),(10,-20)]],					#G
	[[(-10,-20), (-10,20), (-10,0), (10,0), (10,20), (10,-20)]],				#H
	[[(0,20), (0,-20)]],														#I
	[[(-10,20), (0,-20), (0,-20), (-10,-20), (10,-20)]],						#J
	[[(-10,-20), (-10,20), (-10,0), (10,-20), (-10,0), (10,20)]],				#K
	[[(10,20), (-10,20), (-10,-20)]],											#L
	[[(-10,20), (-10,-20), (0,0), (10,-20), (10,20)]],							#M
	[[(-10,20), (-10,-20), (10,20), (10,-20)]],									#N
	[[(-10,20), (-10,-20), (10,-20), (10,20), (-10,20)]],						#O
	[[(-10,0), (10,0), (10,-20), (-10,-20), (-10,20)]],							#P
	[[(10,20), (10,-20), (-10,-20), (-10,20), (10,20),(15,25)]],				#Q
	[[(-10,20), (-10,-20), (10,-20), (10,0), (-10,0), (10,20)]],				#R
	[[(10,-20), (-10,-20), (-10,0), (10,0), (10,20), (-10,20)]],				#S
	[[(0,20), (0,-20), (-10,-20), (10,-20)]],									#T
	[[(-10,-20), (-10,20), (10,20), (10,-20)]],									#U
	[[(-10,-20), (0,20), (10,-20)]],											#V
	[[(-10,-20), (-10,20), (0,0), (10,20), (10,-20)]],							#W
	[[(-10,20), (10,-20)], [(-10,-20), (10,20)]],								#X
	[[(0,20), (0,0), (10,-20), (0,0), (-10,-20)]],								#Y
	[[(10,20), (-10,20), (10,-20), (-10,-20)]],									#Z
	
				
	# A implementer	

	[[(-30,-10), (0,-30), (0,30)], [(-30,30), (30,30)]],							#[
	[[(-30,-10), (0,-30), (30,-10), (30,0), (-30,30), (30,30)]],					#\
	[[(-30,-30), (0,-30), (30,-10), (0,0), (30,10), (0,30), (-30,30)]],				#]
	[[(30,10), (-30,10), (0,-30), (0,30)]],											#^
	[[(30,-30), (-30,-30), (-30,0), (0,0), (30,10), (0,30), (-30,30)]],				#_
	[[(30,-30), (0,-30), (-30,-10), (-30,30), (0,30), (30,10), (30,0), (-30,0)]],	#`
			
	# Implementé
	
	[[(-20,20), (-20,-20), (20,-20), (20,20), (20,0), (-20,0)]],				#a
	[[(-20,20), (-20,-20), (20,-20), (20,20), (-20,20), (-20,0), (20,0)]],		#b
	[[(20,20), (-20,20), (-20,-20), (20,-20)]],									#c
	[[(-20,20), (-20,-20), (20,-20), (20,20), (-20,20)]],						#d
	[[(20,20), (-20,20), (-20,-0), (20,0), (-20,0), (-20,-20), (20,-20)]],		#e
	[[(-20,20), (-20,-0), (20,0), (-20,0), (-20,-20), (20,-20)]],				#f
	[[(0,0), (20,0), (20,20), (-20,20), (-20,-20),(20,-20)]],					#g
	[[(-20,-20), (-20,20), (-20,0), (20,0), (20,20), (20,-20)]],				#H
	[[(0,20), (0,-20)]],														#I
	[[(-20,20), (0,-20), (0,-20), (-20,-20), (20,-20)]],						#J
	[[(-20,-20), (-20,20), (-20,0), (20,-20), (-20,0), (20,20)]],				#K
	[[(20,20), (-20,20), (-20,-20)]],											#L
	[[(-20,20), (-20,-20), (0,0), (20,-20), (20,20)]],							#M
	[[(-20,20), (-20,-20), (20,20), (20,-20)]],									#N
	[[(-20,20), (-20,-20), (20,-20), (20,20), (-20,20)]],						#O
	[[(-20,0), (20,0), (20,-20), (-20,-20), (-20,20)]],							#P
	[[(20,20), (20,-20), (-20,-20), (-20,20), (20,20),(25,25)]],				#Q
	[[(-20,20), (-20,-20), (20,-20), (20,0), (-20,0), (20,20)]],				#R
	[[(20,-20), (-20,-20), (-20,0), (20,0), (20,20), (-20,20)]],				#S
	[[(0,20), (0,-20), (-20,-20), (20,-20)]],									#T
	[[(-20,-20), (-20,20), (20,20), (20,-20)]],									#U
	[[(-20,-20), (0,20), (20,-20)]],											#V
	[[(-20,-20), (-20,20), (0,0), (20,20), (20,-20)]],							#W
	[[(-20,20), (20,-20)], [(-20,-20), (20,20)]],								#X
	[[(0,20), (0,0), (20,-20), (0,0), (-20,-20)]],								#Y
	[[(20,20), (-20,20), (20,-20), (-20,-20)]],									#Z

	[[(-2,15), (2,15)]]															# Point a la place de {

]


class Text(object):
	'''
	classdocs
	'''


	def __init__(self):
		'''
		Constructor
		'''
		self.value = "TEAM LASER TMPLAB"
		self.zoom = ZOOM_PLAYING
		
	def Reset(self):
		self.value = 111
	
	def ZoomIn(self):
		self.zoom += DZOOM_GAMEOVER
		if self.zoom > ZOOM_GAMEOVER:
			self.zoom = ZOOM_GAMEOVER
	
	def ZoomOut(self):
		self.zoom += DZOOM_PLAYING
		if self.zoom < ZOOM_PLAYING:
			self.zoom = ZOOM_PLAYING

	def ZoomReset(self):
		self.zoom = ZOOM_PLAYING
		
	def Draw(self, f):
		value_temp = self.value
		rg_digit = 0
		chars = []
		while rg_digit < 3 or value_temp:
			chars.append(value_temp % 10)
			value_temp //= 10
			rg_digit += 1
		#if gstt.fs == GAME_FS_PLAY:
		#	del chars[0]
		self.DrawChars(f, chars)
	
	def DrawChars(self, f, chars):
		#TODO : gérer correctement les coordonnées
		l = len(chars)
		f.LineTo((text_pos[0],text_pos[1]), 0x80000000)
		for i, ch in enumerate(chars):
			x_offset = 12 * (l - 3*i)
			digit_pl_list = ASCII_GRAPHICS[ch+10]
			
			for pl in digit_pl_list:
				pl_draw = []
				for xy in pl:
					xy_draw = vectors.Vector2D(text_pos[0],text_pos[1]) + vectors.Vector2D(xy[0] + x_offset,xy[1]) * self.zoom
					pl_draw.append(xy_draw.ToTuple())
				f.PolyLineOneColor(pl_draw, 0xFFFFFF)
		
		
		
		