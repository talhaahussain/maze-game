import pygame
pygame.init()

# screen setup
screen_x = 1000
screen_y = 700
fps = 144

# font setup
font_1 = pygame.font.SysFont("segoeui", 20)
font_2 = pygame.font.SysFont("segoeuiblack", 40)

# sound setup
entry_sound = pygame.mixer.Sound("sounds/entry.wav")
exit_sound = pygame.mixer.Sound("sounds/exit.wav")
menu_back_sound = pygame.mixer.Sound("sounds/menu_back.wav")
menu_forward_sound = pygame.mixer.Sound("sounds/menu_forward.wav")
ticking_sound = pygame.mixer.Sound("sounds/singlewind3.wav")
lose_sound = pygame.mixer.Sound("sounds/you_lose.wav")
win_sound = pygame.mixer.Sound("sounds/you_win.wav")

# image setup
timer0_image = pygame.image.load("images/timer/timer0.png")#.convert_alpha()
timer1_image = pygame.image.load("images/timer/timer1.png")#.convert_alpha()
timer2_image = pygame.image.load("images/timer/timer2.png")#.convert_alpha()
timer3_image = pygame.image.load("images/timer/timer3.png")#.convert_alpha()
timer4_image = pygame.image.load("images/timer/timer4.png")#.convert_alpha()
timer5_image = pygame.image.load("images/timer/timer5.png")#.convert_alpha()
timer6_image = pygame.image.load("images/timer/timer6.png")#.convert_alpha()
timer7_image = pygame.image.load("images/timer/timer7.png")#.convert_alpha()
timer8_image = pygame.image.load("images/timer/timer8.png")#.convert_alpha()
timer9_image = pygame.image.load("images/timer/timer9.png")#.convert_alpha()
timer10_image = pygame.image.load("images/timer/timer10.png")#.convert_alpha()
timer11_image = pygame.image.load("images/timer/timer11.png")#.convert_alpha()
timer12_image = pygame.image.load("images/timer/timer12.png")#.convert_alpha()
timer13_image = pygame.image.load("images/timer/timer13.png")#.convert_alpha()
timer14_image = pygame.image.load("images/timer/timer14.png")#.convert_alpha()
timer15_image = pygame.image.load("images/timer/timer15.png")#.convert_alpha()

# colour setup
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
orange = (255, 127, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
indigo = (46, 43, 95)
violet =(139, 0, 255)
