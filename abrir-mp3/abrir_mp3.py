import pygame
pygame.mixer.init()
pygame.base.init()
pygame.mixer.music.load('glad_you_came.mp3')
pygame.mixer.music.play()
pygame.event.wait()
