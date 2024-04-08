import pygame
from assets import *

# Wall class - used for the maze.
class Wall:
    def __init__(self, x, y, size, colour):
        self.x = x 
        self.y = y
        self.size = size
        self.colour = colour
        
    def draw(self, screen):
        pygame.draw.rect(screen, (self.colour), (self.x, self.y, self.size, self.size))
        
# Character class - used for the player to control in the main game.
class Character:
    def __init__(self, x, y, width, height, colour, controls, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.controls = controls
        self.speed = speed
        self.alive = True
        self.move_delay = 65
        self.last_move = pygame.time.get_ticks()
        self.moved = False
        self.moved_x = False
        self.moved_y = False
        

    def draw(self, screen):
        if self.alive == True:
            pygame.draw.rect(screen, self.colour, pygame.Rect((self.x, self.y, self.width, self.height)))

    def wall_collision(self, walls):
        for wall in walls:
            if wall.x == self.x and wall.y == self.y:
                return True # returns True if the character is touching a wall
        return False # if not, returns False
        
    def move(self, walls, timer):
        if self.alive == True:
            now = pygame.time.get_ticks()

            if now - self.last_move > self.move_delay: # implements a slight movement delay
                self.last_move = now

                pressed_keys = pygame.key.get_pressed()   
                if self.alive == True: # the character can only move if they're alive
                    """
                        The following first checks what key has been pressed, and then moves the character in that direction once.
                        It then checks if the character has collided with a wall.
                        If yes, they're moved back to where they were previously.
                    """
                    if pressed_keys[self.controls[0]] and (self.moved_x == False): 
                        self.y -= self.speed
                        if self.wall_collision(walls): 
                            self.y += self.speed
                            self.moved = False
                        else:
                            self.moved = True
                            self.moved_y = True
                       
                        
                    if pressed_keys[self.controls[1]] and (self.moved_x == False):
                        self.y += self.speed
                        if self.wall_collision(walls):
                            self.y -= self.speed
                            self.moved = False
                        else:
                            self.moved = True
                            self.moved_y = True

                    if pressed_keys[self.controls[2]] and (self.moved_y == False):
                        self.x += self.speed
                        if self.wall_collision(walls):
                            self.x -= self.speed
                            self.moved = False
                        else:
                            self.moved = True
                            self.moved_x = True

                    if pressed_keys[self.controls[3]] and (self.moved_y == False):
                        self.x -= self.speed
                        if self.wall_collision(walls):
                            self.x += self.speed
                            self.moved = False
                        else:
                            self.moved = True
                            self.moved_x = True
                            
                    if self.moved == True:
                        timer.reset()
                        self.moved = False
                        
                    if self.moved_x == True:
                        self.moved_x = False
                    
                    if self.moved_y == True:
                        self.moved_y = False
    def die(self):
        self.alive = False

    def reset(self):
        self.alive = True


# Timer class - counts how much more time the player can remain idle before death.
class Timer:
    def __init__(self, x, y, colour, width, height, duration):
        self.x = x
        self.y = y
        self.colour = colour
        self.width = width
        self.height = height
        self.duration = int(duration)
        self.last_tick = pygame.time.get_ticks() # Used to allow the timer to count down
        self.timer_expired = False
        self.sound_played = False
        self.paused = False
        self.original_duration = int(duration)

    def draw(self, screen):
        if self.paused == False: # Only counts down if the timer isn't paused
            """
            if the timer is at 'n' duration, display the image with n seconds left.
            """
            if self.duration == 15: 
                screen.blit(timer15_image, (self.x, self.y))
            elif self.duration == 14:
                screen.blit(timer14_image, (self.x, self.y))
            elif self.duration == 13:
                screen.blit(timer13_image, (self.x, self.y))
            elif self.duration == 12:
                screen.blit(timer12_image, (self.x, self.y))
            elif self.duration == 11:
                screen.blit(timer11_image, (self.x, self.y))
            elif self.duration == 10:
                screen.blit(timer10_image, (self.x, self.y))
            elif self.duration == 9:
                screen.blit(timer9_image, (self.x, self.y))
            elif self.duration == 8:
                screen.blit(timer8_image, (self.x, self.y))
            elif self.duration == 7:
                screen.blit(timer7_image, (self.x, self.y))
            elif self.duration == 6:
                screen.blit(timer6_image, (self.x, self.y))
            elif self.duration == 5:
                screen.blit(timer5_image, (self.x, self.y))
            elif self.duration == 4:
                screen.blit(timer4_image, (self.x, self.y))
            elif self.duration == 3:
                screen.blit(timer3_image, (self.x, self.y))
            elif self.duration == 2:
                screen.blit(timer2_image, (self.x, self.y))
            elif self.duration == 1:
                screen.blit(timer1_image, (self.x, self.y))
            else:
                screen.blit(timer0_image, (self.x, self.y))
                self.expired()
        
        
    def countdown(self):
        if self.paused == False:
            if self.timer_expired == False:
                now = pygame.time.get_ticks()
                if now > self.last_tick + 1000:
                    self.duration -= 1
                    self.last_tick = now
                    ticking_sound.play() 

    def expired(self):
        if self.paused == False:
            self.timer_expired = True
            if self.sound_played == False:
                lose_sound.play()
                self.sound_played = True

    def pause(self):
        self.paused = True

    def reset(self):
        self.timer_expired = False
        self.sound_played = False
        self.duration = self.original_duration


# Lava class - used to trail the player in the main game.
class Lava:
    def __init__(self, x, y, size, colour):
        self.x = x
        self.y = y
        self.width = size
        self.height = size
        self.colour = colour
        self.touching = False

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, pygame.Rect((self.x, self.y, self.width, self.height)))

    def check_touching(self, character, timer):
        if (character.x == self.x) and (character.y == self.y):            
            self.touching_player(character, timer)
            
    def touching_player(self, character, timer):
        character.die()
        timer.duration = 0 # Sets the duration to 0, killing the player


# Goal class (child of lava) - a single cell that the player must reach to win.
# Operates similarly to the lava, except triggers victory.
class Goal(Lava):
    def __init__(self, x, y, size, colour):
        Lava.__init__(self, x, y, size, colour) # Initialises as a lava cell...
        # ...but has two more attributes
        self.sound_played = False 
        self.win = False

    def check_touching(self, character, timer):
        if (character.x == self.x) and (character.y == self.y):
            self.touching_player(character, timer)

    def touching_player(self, character, timer):
        if self.sound_played == False:
            win_sound.play()
            self.sound_played = True
            self.won(timer, character)

    def won(self, timer, character):
        self.win = True
        timer.pause()
        character.die()
    
        
