# coding=UTF-8

import ConfigParser

# Doc : http://python.jpvweb.com/python/mesrecettespython/doku.php?id=fichier_de_configuration

config = ConfigParser.ConfigParser()
config.read("testsettings.conf")
centerx = config.getint('laser1', 'centerx')
centery = config.getint('laser1', 'centery')

print centerx,centery 


'''

# Doc : http://python.jpvweb.com/python/mesrecettespython/doku.php?id=fichier_de_configuration

# en string :
# config.get
# config.getfloat()
# config.getboolean()

cfg.set('Section2', 'cle22', 'valeur22_modif')

Et, bien sûr, n'oubliez pas de ré-écrire le fichier sur disque après toutes ces modifications!
config.write(open('testsettings.conf','w'))


'''



