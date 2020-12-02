import pygame, sys
 

Clock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Hunting Town Bordeaux')
screen = pygame.display.set_mode((500, 500))



font = pygame.font.SysFont(None, 20)
 
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
click = False
 
def main_menu():
    

    while True:
 
        screen.fill((0,0,0))
        #Chargement et collage du fond
        # fond = pygame.image.load("Bordeaux.png")
        # rect = fond.get_rect()
        # screen.blit(fond,rect)
        # pygame.display.flip()
        # continuer = 1
        # while continuer:
	    #     continuer = int(input())

        draw_text('MENU', font, (255, 255, 255), screen, 20, 20)
 
        mx, my = pygame.mouse.get_pos()
 
        button_1 = pygame.Rect(120, 100, 50, 50)
        draw_text('ENIGME', font, (255, 255, 255), screen, 30, 125)
        button_2 = pygame.Rect(120, 200, 50, 50)
        draw_text('MAP', font, (255, 255, 255), screen, 30, 225)
        button_3 = pygame.Rect(120, 300, 50, 50)
        draw_text('MESSAGERIE', font, (255, 255, 255), screen, 30, 325)
        if button_1.collidepoint((mx, my)):
            if click:
                enigme()
        if button_2.collidepoint((mx, my)):
            if click:
                map()
        if button_3.collidepoint((mx, my)):
            if click:
                messagerie()

        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
        pygame.draw.rect(screen, (255, 0, 0), button_3)
 
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        Clock.tick(60)
 
def enigme():
    running = True
    while running:
        screen.fill((0,0,0))
        
        draw_text('ENIGME', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        Clock.tick(60)
 
def map():
    running = True
    while running:
        screen.fill((0,0,0))
 
        draw_text('MAP', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        Clock.tick(60)

def messagerie():
    running = True
    while running:
        screen.fill((0,0,0))
 
        draw_text('MESSAGERIE', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        Clock.tick(60)
 
main_menu()