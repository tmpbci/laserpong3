# coding=UTF-8

# Laser Pong
#
# by Sam Neurohack
#
# Based on Laser Pinball
#


'''
---------------------
Exception: must be str, not bytes
- - - - - - - - - - -
  File "main.py", line 57, in dac_thread
    d = dac.DAC(etherIP)
  File "/Users/leduc/Desktop/laserpong3/dac.py", line 137, in __init__
    first_status = self.readresp("?")
  File "/Users/leduc/Desktop/laserpong3/dac.py", line 111, in readresp
    data = self.read(22)
  File "/Users/leduc/Desktop/laserpong3/dac.py", line 103, in read
    self.buf += self.conn.recv(4096)
'''

import pygame

# STDLIB
import math
import itertools
import sys
import os

import threading
import time
import random

from globalVars import *
import gstt
import ball
import score
import score2
import borders
import filet
import flips
import logo
import text

import frame
from vectors import Vector2D
import renderer
import dac

import argparse
import configparser

config = configparser.ConfigParser()
config.read("settings.conf")
	
def StartPlaying(first_time = False):
	gstt.score.Reset()
	gstt.score2.Reset()
	gstt.fs = GAME_FS_LAUNCH
	gstt.x = ball_origin[0]
	gstt.y = ball_origin[1]

	
def dac_thread():

	while True:
		try:
			#etherIP = dac.find_first_dac()
			print(type(etherIP),etherIP)
			d = dac.DAC(etherIP)
			d.play_stream(laser)

		except Exception as e:

			import sys, traceback
			print ('\n---------------------')
			print ('Exception: %s' % e)
			print ('- - - - - - - - - - -')
			traceback.print_tb(sys.exc_info()[2])
			print ("\n")

def getHats():

			gstt.pad1up = pad1.get_hat(0)[1]

			if pad1.get_hat(0)[1] == -1:
				gstt.pad1down = 1
				gstt.pad1up = 0
			else:
				gstt.pad1down = 0	
			print (pad1.get_hat(0)[1],gstt.pad1up,gstt.pad1down)
			
			gstt.pad2up = pad2.get_hat(0)[1]

			if pad2.get_hat(0)[1] == -1:
				gstt.pad2down = 1
				gstt.pad2up = 0
			else:
				gstt.pad2down = 0	
			print (pad2.get_hat(0)[1],gstt.pad2up,gstt.pad2down)


def DrawTestPattern(f):
	l,h = screen_size
	L_SLOPE = 30
	
	f.Line((0, 0), (l, 0), 0xFFFFFF)
	f.LineTo((l, h), 0xFFFFFF)
	f.LineTo((0, h), 0xFFFFFF)
	f.LineTo((0, 0), 0xFFFFFF)
	
	f.LineTo((2*L_SLOPE, h), 0)
	for i in xrange(1,7):
		c = (0xFF0000 if i & 1 else 0) | (0xFF00 if i & 2 else 0) | (0xFF if i & 4 else 0)
		f.LineTo(((2 * i + 1) * L_SLOPE, 0), c)
		f.LineTo(((2 * i + 2) * L_SLOPE, h), c)
	f.Line((l*.5, h*.5), (l*.75, -h*.5), 0xFF00FF)
	f.LineTo((l*1.5, h*.5), 0xFF00FF)
	f.LineTo((l*.75, h*1.5), 0xFF00FF)
	f.LineTo((l*.5, h*.5), 0xFF00FF)
		

def WriteSettings(): 

	config.set('laser1', 'centerx', str(gstt.centerx))
	config.set('laser1', 'centery', str(gstt.centery))
	config.set('laser1', 'zoomx', str(gstt.zoomx))
	config.set('laser1', 'zoomy', str(gstt.zoomy))
	config.set('laser1', 'sizex', str(gstt.sizex))
	config.set('laser1', 'sizey', str(gstt.sizey))
	config.set('laser1', 'finangle', str(gstt.finangle))
	config.set('laser1', 'swapx', str(gstt.swapx))
	config.set('laser1', 'swapy', str(gstt.swapy))
	config.write(open('settings.conf','w'))

def ReadSettings(): 
	
	gstt.centerx = config.getint('laser1', 'centerx')
	gstt.centery = config.getint('laser1', 'centery')
	gstt.zoomx = config.getfloat('laser1', 'zoomx')
	gstt.zoomy = config.getfloat('laser1', 'zoomy')
	gstt.sizex = config.getint('laser1', 'sizex')
	gstt.sizey = config.getint('laser1', 'sizey')
	gstt.finangle = config.getfloat('laser1', 'finangle')
	gstt.swapx = config.getint('laser1', 'swapx')
	gstt.swapy = config.getint('laser1', 'swapy')


	print ("setttings : ")
	print (str(gstt.centerx) + "," + str(gstt.centery) + "," + str(gstt.zoomx) + "," + str(gstt.zoomy) + "," + str(gstt.sizex) + "," + str(gstt.sizey) + "," + str(gstt.finangle)  + "," + str(gstt.swapx) + "," + str(gstt.swapy))


		
def Align(f):

	l,h = screen_size
	L_SLOPE = 30
	
	f.Line((0, 0), (l, 0), 0xFFFFFF)
	f.LineTo((l, h), 0xFFFFFF)
	f.LineTo((0, h), 0xFFFFFF)
	f.LineTo((0, 0), 0xFFFFFF)
	laser = renderer.LaserRenderer(fwork_holder, gstt.centerx, gstt.centery, gstt.zoomx, gstt.zoomy, gstt.sizex, gstt.sizey)

	print (str(gstt.centerx) + "," + str(gstt.centery) + "," + str(gstt.zoomx) + "," + str(gstt.zoomy) + "," + str(gstt.sizex) + "," + str(gstt.sizey) + "," + str(gstt.finangle)  + "," + str(gstt.swapx) + "," + str(gstt.swapy))
	
	WriteSettings()





# Read settings

ReadSettings()



# Parse args if needed

print ("")
print ("Arguments parsing if needed...")
argsparser = argparse.ArgumentParser(description="Laserpong")
argsparser.add_argument("-x","--invx",help="Invert X axis",action="store_true")
argsparser.add_argument("-y","--invy",help="Invert Y axis",action="store_true")
argsparser.add_argument("-s","--save",help="Save to settings file",action="store_true")
argsparser.add_argument("-l1","--laser1",help="For Laser '1' : last digit of etherdream ip address 192.168.1.0/24 (4 by default). Localhost if digit provided is 0.",type=int)

args = argsparser.parse_args()



if args.invx:
	print("X inverted")
	gstt.swapx = -1
else:
	print ("X not Inverted")
	gstt.swapx = 1



if args.invy:
	print("Y inverted")
	gstt.swapy = -1
else:
	print ("Y not Inverted")
	gstt.swapy = 1


# todo : handle several lasers and save in settings.conf

print(args.laser1)

if args.laser1 != None:
	print(args.laser1)
	lstdgtlaser = args.laser1
	if lstdgtlaser == 0:
		etherIP = '127.0.0.1'
	else:
		etherIP = "192.168.1."+str(lstdgtlaser)


else:
	etherIP = '192.168.1.4'
	

print ("Laser 1 etherIP:",etherIP)


if args.save:
	print("New parameters saved")
	WriteSettings()


#exit(0)

# Inits
	
app_path = os.path.dirname(os.path.realpath(__file__))

pygame.init()

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Laser Pong")
clock = pygame.time.Clock()

fwork_holder = frame.FrameHolder()
laser = renderer.LaserRenderer(fwork_holder, gstt.centerx, gstt.centery, gstt.zoomx, gstt.zoomy, gstt.sizex, gstt.sizey)


dac_threading = threading.Thread(target=dac_thread, args=[])
dac_threading.start()

update_screen = False

gstt.score = score.Score()
gstt.score2 = score2.Score2()
gstt.bll = ball.Ball()
gstt.flp = flips.Flips()
gstt.txt = text.Text()
gstt.flt = filet.Filet()
gstt.brdrs = borders.Borders()
gstt.xvel = - 1
gstt.yvel = 0
gstt.lscore = 0
gstt.rscore = 0
gstt.ly = FLIPS_lorigin[1]
gstt.ry = FLIPS_rorigin[1]
flipsy = [gstt.ly, gstt.ry]
gstt.stick = 0
gstt.x = ball_origin[0]
gstt.y = ball_origin[1]
gstt.remain = BALL_MAX	



# Joypads ?

print ("")
Nbpads = pygame.joystick.get_count()
print ("Joypads : ", str(Nbpads))

if Nbpads > 1:

	pad2 = pygame.joystick.Joystick(1)
	pad2.init()

	print (pad2.get_name())
	print ("Axis : ", str(pad2.get_numaxes()))
	numButtons = pad2.get_numbuttons()
	print ("Buttons : " , str(numButtons))

if Nbpads > 0:

	pad1 = pygame.joystick.Joystick(0)
	pad1.init()

	print (pad1.get_name())


	print ("Axis : ", str(pad1.get_numaxes()))
	numButtons = pad1.get_numbuttons()
	print ("Buttons : " , str(numButtons))


keystates = pygame.key.get_pressed()

gstt.fs = GAME_FS_MENU



# Run !

while gstt.fs != GAME_FS_QUIT:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gstt.fs = GAME_FS_QUIT
	
	keystates_prev = keystates[:]
	keystates = pygame.key.get_pressed()[:]


	# Etats du jeu
	
	
	if gstt.fs == GAME_FS_MENU:
		
		
		if keystates[pygame.K_ESCAPE] and not keystates_prev[pygame.K_ESCAPE]:
			gstt.fs = GAME_FS_QUIT
		
		elif keystates[pygame.K_SPACE] and not keystates_prev[pygame.K_SPACE]:
			StartPlaying(True)
		gstt.lscore = 0
		gstt.rscore = 0
		


	elif gstt.fs == GAME_FS_PLAY:


		if keystates[pygame.K_ESCAPE] and not keystates_prev[pygame.K_ESCAPE]:
			gstt.fs = GAME_FS_MENU
		
		if Nbpads > 0:
			print ("pad state")
			print (pad1.get_button(0),pad1.get_button(1),pad1.get_button(2),pad1.get_button(3))
		
		
		
		# Ball is out on left side ?
		if gstt.x < FLIPS_lorigin[0] + PADDLE_width:

			print ("ball.y : ", gstt.y, " ly : ", gstt.ly)
			
			if gstt.y > (gstt.ly + PADDLE_height + 1) or gstt.y < (gstt.ly - BALL_SIZE_Y - 1):
				gstt.score.Increase(1)
				gstt.rscore += 1
				gstt.xvel = random.uniform(-1,-0.6)
				
				if gstt.rscore == 11:
					gstt.fs = GAME_FS_MENU
				
				else: 
					gstt.fs = GAME_FS_LAUNCH
			
			else:
				gstt.x = FLIPS_lorigin[0] + PADDLE_width
				gstt.xvel *= -1
			
		
		
		# Ball is out on right side ?
		if gstt.x > FLIPS_rorigin[0] - PADDLE_width:
		
			print ("ball.y : ", gstt.y, " ry : ", gstt.ry)

			if gstt.y < (gstt.ry - BALL_SIZE_Y - 1) or gstt.y > (gstt.ry + PADDLE_height + 1):
				gstt.score2.Increase(1)
				gstt.lscore += 1
				gstt.xvel = random.uniform(1,0.6)
				
				if gstt.lscore == 11:
					gstt.fs = GAME_FS_MENU
				else: 
					gstt.fs = GAME_FS_LAUNCH
					
			else:
				gstt.xvel *= -1
				gstt.x = FLIPS_rorigin[0] - PADDLE_width	
				

		
		# top wall ? 
		if gstt.y < 0:
			gstt.y = 1
			gstt.yvel *= -1
			
		'''
		if gstt.x < FLIPS_lorigin[0] + PADDLE_width:
			gstt.x = FLIPS_lorigin[0] + PADDLE_width
			gstt.xvel *= -1
			
		if gstt.x > screen_size[0] - PADDLE_width:
			gstt.x = screen_size[0] - PADDLE_width
			gstt.xvel *= -1
		'''
		
		
		# Bottom wall ? 
		if gstt.y > screen_size[1]:
			gstt.y = screen_size[1] - 1
			gstt.yvel *= -1
			
		
		
		# Anim 
		gstt.x += BALL_SPEED * gstt.xvel 
		gstt.y += BALL_SPEED * gstt.yvel
		gstt.yvel += GRAVITY
		gstt.bll.Move(gstt.x,gstt.y)
		
		if  Nbpads > 0:
			getHats()
			flipsy =  gstt.flp.Move(gstt.pad1up,gstt.pad1down,gstt.pad2up,gstt.pad2down)
		
		else:
			flipsy =  gstt.flp.Move(keystates[pygame.K_a],keystates[pygame.K_q],keystates[pygame.K_UP],keystates[pygame.K_DOWN])
		
		gstt.ly = flipsy[0]
		gstt.ry = flipsy[1]

		
	

	elif gstt.fs == GAME_FS_LAUNCH:
	
	
		
		if keystates[pygame.K_ESCAPE] and not keystates_prev[pygame.K_ESCAPE]:
			gstt.fs = GAME_FS_MENU
	
		if keystates[pygame.K_SPACE] and not keystates_prev[pygame.K_SPACE]:
			gstt.fs = GAME_FS_PLAY
			#gstt.xvel = 0
			gstt.yvel = 0
			
			while math.fabs(gstt.xvel + gstt.yvel) < 1:
				gstt.yvel = random.uniform(-1,1)
			
		gstt.x = ball_origin[0]
		gstt.y = ball_origin[1]
		gstt.bll.Move(gstt.x,gstt.y)
		if  Nbpads > 0:
			getHats()
			flipsy =  gstt.flp.Move(gstt.pad1up,gstt.pad1down,gstt.pad2up,gstt.pad2down)
			
		else:
			flipsy =  gstt.flp.Move(keystates[pygame.K_a],keystates[pygame.K_q],keystates[pygame.K_UP],keystates[pygame.K_DOWN])
		gstt.ly = flipsy[0]
		gstt.ry = flipsy[1]



	elif gstt.fs == GAME_FS_GAMEOVER:
	

		#TODO : MODE GAME OVER, autres opérations d'animation
		# Remarque : on peut supprimer le mode GAME OVER et le gérer dans le mode jeu
		# si les traitements sont les mêmes

		if keystates[pygame.K_SPACE] and not keystates_prev[pygame.K_SPACE]:
			StartPlaying(False)
		elif keystates[pygame.K_ESCAPE] and not keystates_prev[pygame.K_ESCAPE]:
			gstt.fs = GAME_FS_MENU



	# OPERATIONS D'AFFICHAGE


	# On efface l'écran avant
	screen.fill(0)

	# Création de la nouvelle frame vide où les objets du jeu vont dessiner
	fwork = frame.Frame()
	
	
	# Touches d'alignement
	if keystates[pygame.K_p]:
		DrawTestPattern(fwork)
		
	if keystates[pygame.K_x]:
		Align(fwork)
		
	if keystates[pygame.K_r]:
		gstt.centerx += 20
		Align(fwork)

	if keystates[pygame.K_t]:
		gstt.centerx -= 20
		Align(fwork)
		
	if keystates[pygame.K_y]:
		gstt.centery += 20
		Align(fwork)

	if keystates[pygame.K_u]:
		gstt.centery -= 20
		Align(fwork)

	if keystates[pygame.K_f]:
		gstt.zoomx += 0.1
		Align(fwork)

	if keystates[pygame.K_g]:
		gstt.zoomx -= 0.1
		Align(fwork)
		
	if keystates[pygame.K_h]:
		gstt.zoomy += 0.1
		Align(fwork)

	if keystates[pygame.K_j]:
		gstt.zoomy -= 0.1
		Align(fwork)
	
	if keystates[pygame.K_c]:
		gstt.sizex -= 50
		Align(fwork)
		
	if keystates[pygame.K_v]:
		gstt.sizex += 50
		Align(fwork)
		
	if keystates[pygame.K_b]:
		gstt.sizey -= 50
		Align(fwork)
		
	if keystates[pygame.K_n]:
		gstt.sizey += 50
		Align(fwork)
		
		
	if keystates[pygame.K_l]:
		gstt.finangle -= 0.001
		Align(fwork)
		
	if keystates[pygame.K_m]:
		gstt.finangle += 0.001
		Align(fwork)



	# Genere les listes de points selon l'état du jeu.
	else:
		display_plyr = gstt.fs == GAME_FS_PLAY or gstt.fs == GAME_FS_GAMEOVER or gstt.fs == GAME_FS_LAUNCH
		if display_plyr:
			
			gstt.score.Draw(fwork)
			gstt.score2.Draw(fwork)
			gstt.flp.Draw(fwork)
			gstt.bll.Draw(fwork)
			gstt.flt.Draw(fwork)

		if gstt.fs == GAME_FS_MENU:
			logo.Draw(fwork)
	


	# Affecter la frame construite à l'objet conteneur de frame servant au système de rendu par laser
	fwork_holder.f = fwork

	if update_screen:
		update_screen = False
		fwork.RenderScreen(screen)
		pygame.display.flip()
	else:
		update_screen = True

	
	# TODO : rendre indépendante la fréquence de rafraîchissement de l'écran par
	# rapport à celle de l'animation du jeu
	clock.tick(100)

pygame.quit()

