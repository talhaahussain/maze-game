import pygame
from assets import *

from pygame.locals import *
pygame.init()


class Textbox:
    def __init__(self, x, y, colour, text, name, width, height, font):
        self.name = name # name of the textbox
        self.colour = colour # colour of the textbox
        self.text = str(text) # text on the textbox
        self.font = font # font used with the text
        self.txt = font.render(self.text, True, ((black))) # renders the text in pygame
        self.alt_txt = font.render(self.text, True, ((self.colour)))
        self.rect = pygame.Rect((x, y, width, height)) # stores the coordinates, width and height of the rectangle
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, self.rect) # draws the textbox
        pygame.draw.rect(screen, black, self.rect, 1) # draws the outline
        txt_rect = self.txt.get_rect(center=self.rect.center) # draws the text to the center of the textbox
        screen.blit(self.txt, txt_rect) # draws the text

        
class Button:
    def __init__(self, x, y, colour, text, name, width, height, font, function):
        self.name = name # name of the button
        self.colour = colour # colour of the button
        self.text = str(text) # text on the button
        self.font = font # font used with the text
        self.txt = font.render(self.text, True, ((black))) # renders the text in pygame
        self.alt_txt = font.render(self.text, True, ((self.colour)))
        self.rect = pygame.Rect((x, y, width, height)) # stores the coordinates, width and height of the rectangle
        self.clicked = False # determines whether the button is currently clicked
        self.function = function # stores the function to be called when the button is clicked

    def draw(self, screen):
        if self.clicked == False:
            pygame.draw.rect(screen, self.colour, self.rect) # draws the button
            pygame.draw.rect(screen, black, self.rect, 5) # draws the outline
            txt_rect = self.txt.get_rect(center=self.rect.center) # draws the text to the center of the button
            screen.blit(self.txt, txt_rect) # draws the text
        else:
            pygame.draw.rect(screen, black, self.rect) # draws the button
            pygame.draw.rect(screen, self.colour, self.rect, 5) # draws the outline
            txt_rect = self.alt_txt.get_rect(center=self.rect.center) # draws the text to the center of the button
            screen.blit(self.alt_txt, txt_rect) # draws the text
                
    def check_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN: # if the mouse is clicked...
            if self.rect.collidepoint(pygame.mouse.get_pos()) == True: # ...and the mouse is on the button...
                self.clicked = True # the button is clicked.
                #self.is_clicked() # call 'is_clicked'
        elif event.type == pygame.MOUSEBUTTONUP: # when the button is released...
            if self.clicked: # if it WAS clicked...
                self.function() # calls the appropriate function
            self.clicked = False # sets the button to unclicked once again, as the button is released
   
