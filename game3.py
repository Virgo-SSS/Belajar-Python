import pygame
from pygame.locals import *
import math

# init pygame nya
pygame.init()

# atur ukuran canvas nya atau ukuran window nya dan nama game nya
pygame.display.set_caption("TEMBAK TEMBAK AN")
width = 600
height = 600
win = pygame.display.set_mode((width, height))

# Membuat controler movement position  W A S D 
keys = {
    "top" : False,
    "bottom" : False,
    "left" : False,
    "Right" : False

}

# variable untuk membuat looping game nya
run = True

# menentukan posisi awal player
playerpos = [100, 100]

# memasukan resource game
player = pygame.image.load("tutorial-pygame-master/resources/images/dude.png")
rumput = pygame.image.load("tutorial-pygame-master/resources/images/grass.png")
kastil = pygame.image.load("tutorial-pygame-master/resources/images/castle.png")


# bikin looping agar game nya tidak terclose
while run:
    # bershikan screen jadi kosong
    win.fill(0)
    # menggambar rumput
    for x in range (int(width/rumput.get_width()+1)):
        for y in range (int(width/rumput.get_height()+1)):
            win.blit(rumput, (x*100, y*100))
    
    # Menggambar kastil nya
    win.blit(kastil,(0,30))
    win.blit(kastil,(0,135))
    win.blit(kastil,(0,240))
    win.blit(kastil,(0,345))
    
    # mengubah arah object player mengikuti mouse menggunakan rumus tangen 
    # posisi playerpos [100, 100] (ada diatas)
    # HELP GUYS GK NGERTI SAMA SEKALI RUMUS TANGEN NYA DIMANA :")
    mouse_position = pygame.mouse.get_pos()
    angle = math.atan2(mouse_position[1] - (playerpos[1]+32), mouse_position[0] - (playerpos[0]+26))
    player_rotation = pygame.transform.rotate(player, 360 - angle * 57.29)
    new_playerpos = (playerpos[0] - player_rotation.get_rect().width / 2, playerpos[1] - player_rotation.get_rect().height / 2)
    win.blit(player_rotation, new_playerpos) #posisi baru player
    
    # untuk mengupdate screen
    pygame.display.flip()

    # looping untuk isi game
    for event in pygame.event.get():
        # eexit
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        # Mmebuat key  down dan key up (maksud nya ketika keyboard di tekan klik dan di lepas klik nya jadi down up)
        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                keys["top"] = True
            elif event.key == K_a:
                keys ["left"] = True
            elif event.key == K_s:
                keys ["bottom"] = True
            elif event.key == K_d:
                keys ["Right"] = True

        if event.type == pygame.KEYUP:
            if event.key == K_w:
                keys["top"] = False
            elif event.key == K_a:
                keys ["left"] = False
            elif event.key == K_s:
                keys ["bottom"] = False
            elif event.key == K_d:
                keys ["Right"] = False
    # AKHIRAN DARI LOOPING GAME NYA 

    # Membuat movement player
    if keys["top"]:
        playerpos[1] -= 5  #Kurangi nilai y
    elif keys["bottom"]:
        playerpos[1] += 5 #kurangin nilai y
    if keys["left"]:
        playerpos[0] -= 5 #kurangin nilai x
    elif keys["Right"]:
        playerpos[0] += 5 #kurangin nilai x