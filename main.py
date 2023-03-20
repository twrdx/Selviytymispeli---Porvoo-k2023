import pygame

#pygame alustus ja pelialueen luonti
pygame.init()
pelialue = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Selviytymispeli')

#Asetetaan pelialueen väri
tausta = (204, 221, 255)

#Hiiri
mouse = pygame.mouse.get_pos()

#Pelaaja
pelaaja = pygame.Rect(mouse[0], mouse[1], 30, 30)
pelaajan_kuva = pygame.image.load("donut3.png")
pelaajan_kuva.convert()
pelaajan_kuva = pygame.transform.scale(pelaajan_kuva, (30, 30))

#Vihollinen
vihollinen = pygame.Rect(0, 0, 40, 20)
vihollinen_nopeus = [3, 1]

#räjähdys
rajahdyskuva = pygame.image.load("explosion.png")
rajahdyskuva.convert()
pygame.transform.scale(rajahdyskuva, (70, 70))

FPS = 30 
FramePerSec = pygame.time.Clock()

while True:
	#event handler
	for event in pygame.event.get():
		mouse = pygame.mouse.get_pos()
		print(mouse)
		
	pelaaja = pygame.Rect(mouse[0] - 12.5, mouse[1] - 12.5, 25, 25)

	if(vihollinen.right > 400):
		vihollinen_nopeus[0] = vihollinen_nopeus[0] * -1
	if(vihollinen.bottom > 200):
		vihollinen_nopeus[1] = vihollinen_nopeus[1] * -1
	if(vihollinen.left < 0):
		vihollinen_nopeus[0] = vihollinen_nopeus[0] * -1
	if(vihollinen.top < 0):
		vihollinen_nopeus[1] = vihollinen_nopeus[1] * -1

	pelialue.fill(tausta)
	pelialue.blit(pelaajan_kuva, pelaaja)

	FramePerSec.tick(FPS)
	#tämän pitää olla viimeinen rivi koodissa:
	pygame.display.update()