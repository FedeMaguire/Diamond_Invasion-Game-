import pygame
from settings import Settings

class Background(pygame.sprite.Sprite):

    def __init__(self):
        self.screen_width = 1280
        self.screen_height = 800
        self.surf = pygame.image.load("images/Purple Nebula 1 - 1024x1024.png")
        background_width = self.screen_width
        background_height = (background_width/self.surf.get_width())*self.surf.get_height()
        self.surf = pygame.transform.scale(self.surf, (background_width, background_width))
        self.rect = self.surf.get_rect(
            bottomleft=(0,self.screen_height)
        )
        # Used 2 surfaces to generate a better loop for background
        # they move toguether to create a beter flow
        
        self.surf2 = self.surf
        self.rect2 = self.surf2.get_rect(
            bottomleft=self.rect.topleft
        )
        self.ypos = 0
        self.ypos2 = background_height

    def update(self, background_speed):
        self.ypos += .05 * background_speed
        self.ypos2 += .05 * background_speed
        self.rect.y = int(self.ypos)
        self.rect2.y = int(self.ypos2)
        if self.rect.y > self.screen_height:
            self.ypos = self.rect2.y - self.surf2.get_height()
            self.rect.y = self.ypos
        if self.rect2.y > self.screen_height:
            self.ypos2 = self.rect.y - self.surf.get_height()
            self.rect2.y = self.ypos2

    def render(self, dest):
        dest.blit(self.surf, self.rect)
        dest.blit(self.surf2, self.rect2)