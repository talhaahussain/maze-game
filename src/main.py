''' Imports all needed modules and libraries.'''
import time
import pygame
from pygame.locals import *
from maze_algorithm import *
from ui_elements import *
from characters import *
from assets import *
entry_sound.play()

""" 
The states class.
This is simply a template, which every state shall inherit methods and attributes from.
The subclasses may also add their own methods and attributes according to their needs.
"""
class States:
    # The share dictionary holds information to be shared between states.
    share = {
        "keys": [K_w, K_s, K_d, K_a],
        "x_cells": 20,
        "y_cells": 20,
        "timer": 15,
        "easy_wins": 0,
        "medium_wins": 0,
        "hard_wins": 0,
        "current_difficulty": None,
        "current_controls": "WASD",
        }
    def __init__(self):
        self.running = True
        self.next = None
        self.quit = False

    def setup(self):
        pass

    def cleanup(self):
        pass

    def handle_events(self, event):
        pass

    def update(self):
        pass

    def render(self, screen):
        pass

class Main_Menu(States): # The state for the main menu.
    def __init(self):
        States.__init__(self) # Initialises the state using the States superclass constructor.

    def setup(self):
        self.running = True
        """
        Instantiates all buttons and textboxes.
        """
        self.title = Textbox((screen_x/2)-250, screen_y/9, red, "THE FLOOR IS LAVA", "title_textbox", 500, 100, font_2)
        self.play = Button((screen_x/2)-100, screen_y-500, yellow, "PLAY", "play_button", 200, 50, font_1, self.switch_play)
        self.instructions = Button((screen_x/2)-100, screen_y-400, yellow, "INSTRUCTIONS", "instructions_button", 200, 50, font_1, self.switch_instructions)
        self.controls = Button((screen_x/2)-100, screen_y-300, yellow, "CONTROLS", "controls_button", 200, 50, font_1, self.switch_controls)
        self.quit_button = Button((screen_x/2)-100, screen_y-200, yellow, "QUIT", "quit_button", 200, 50, font_1, self.quit_game)
        self.easy_wins_textbox = Textbox((screen_x/2)-250, screen_y/9 - 25, orange, "EASY WINS: " + str(self.share["easy_wins"]), "easy_wins", 500/3, 25, font_1)
        self.medium_wins_textbox = Textbox((screen_x/2)-(250/3), screen_y/9 - 25, orange, "MEDIUM WINS: " + str(self.share["medium_wins"]), "medium_wins", 500/3, 25, font_1)
        self.hard_wins_textbox = Textbox((screen_x/2)+(250/3), screen_y/9 - 25, orange, "HARD WINS: " + str(self.share["hard_wins"]), "hard_wins", 500/3, 25, font_1)
        
        
    def cleanup(self):
        """
        Deletes all buttons and textboxes.
        """
        del self.title, self.play, self.instructions, self.quit_button, self.easy_wins_textbox, self.medium_wins_textbox, self.hard_wins_textbox

    def switch_play(self):
        """
        Directs to the difficulty select state.
        """
        self.next = "difficulty_select"
        menu_forward_sound.play()
        self.running = False

    def switch_instructions(self):
        """
        Directs to the instructions state.
        """
        self.next = "instructions_screen"
        menu_forward_sound.play()
        self.running = False

    def switch_controls(self):
        """
        Directs to the controls select state.
        """
        self.next = "controls_screen"
        menu_forward_sound.play()
        self.running = False

    def quit_game(self):
        """
        Exits the game.
        """
        exit_sound.play()
        self.quit = True        

    def handle_events(self, event):
        """
        Checks if any buttons have been clicked.
        """
        self.play.check_clicked(event)
        self.instructions.check_clicked(event)
        self.controls.check_clicked(event)
        self.quit_button.check_clicked(event)

    def update(self):
        pass

    def render(self, screen):
        """
        Fills the screen with black and draws buttons and textboxes.
        """
        screen.fill(black)
        self.title.draw(screen)
        self.play.draw(screen)
        self.instructions.draw(screen)
        self.controls.draw(screen)
        self.quit_button.draw(screen)
        self.easy_wins_textbox.draw(screen)
        self.medium_wins_textbox.draw(screen)
        self.hard_wins_textbox.draw(screen)

        
class Instructions(States):
    def __init__(self):
        States.__init__(self)

    def setup(self):
        """
        Instantiates all buttons and textboxes.
        """
        self.running = True
        self.title = Textbox((screen_x/2)-250, screen_y/9, red, "INSTRUCTIONS", "title_textbox", 500, 100, font_2)
        """
        The following 5 objects are textboxes that contain the instructions.
        """
        self.instructions_1 = Textbox((screen_x/2)-450, screen_y - 500, orange,
                                    "• Choose your difficulty and navigate your way through the maze, to the yellow goal.",
                                    "instructions_textbox", 900, 50, font_1)
        self.instructions_2 = Textbox((screen_x/2)-450, screen_y - 450, orange,
                                    "• As you move through the maze, deadly lava will trail in your wake, so be careful.",
                                    "instructions_textbox", 900, 50, font_1)
        self.instructions_3 = Textbox((screen_x/2)-450, screen_y - 400, orange,
                                    "• You have to think fast and precisely – a timer will be counting down, and can only be reset if you move.",
                                    "instructions_textbox", 900, 50, font_1)
        self.instructions_4 = Textbox((screen_x/2)-450, screen_y - 350, orange,
                                    "• If the timer expires, the lava will engulf you, and you will fail.",
                                    "instructions_textbox", 900, 50, font_1)
        self.instructions_5 = Textbox((screen_x/2)-450, screen_y - 300, orange,
                                    "• Have fun and good luck!",
                                    "instructions_textbox", 900, 50, font_1)
        """
        The back button, to return the player to the main menu.
        """
        self.back = Button((screen_x/2)-100, screen_y-200, yellow, "BACK", "back_button", 200, 50, font_1, self.switch_main_menu)

    def cleanup(self):
        """
        Deletes all buttons and textboxes.
        """
        del self.title, self.instructions_1, self.instructions_2, self.instructions_3, self.instructions_4, self.instructions_5, self.back

    def switch_main_menu(self):
        """
        Directs to the main menu state.
        """
        self.next = "main_menu"
        menu_back_sound.play()
        self.running = False      

    def handle_events(self, event):
        """
        Checks if the back button has been clicked.
        """
        self.back.check_clicked(event)

    def update(self):
        pass

    def render(self, screen):
        """
        Draws all UI elements to the screen.
        """
        screen.fill(black)
        self.title.draw(screen)
        self.instructions_1.draw(screen)
        self.instructions_2.draw(screen)
        self.instructions_3.draw(screen)
        self.instructions_4.draw(screen)
        self.instructions_5.draw(screen)
        self.back.draw(screen)


class Controls_Setup(States):
    def __init__(self):
        States.__init__(self)

    def setup(self):
        self.running = True
        self.title = Textbox((screen_x/2)-250, screen_y/9, red, "CONTROLS", "title_textbox", 500, 100, font_2)
        # The following button takes 'switch_to_wasd' as a method. It calls this method when it's clicked.
        self.wasd = Button((screen_x/2)-100, screen_y-400, yellow, "SELECT: WASD", "instructions_button", 200, 50, font_1, self.switch_to_wasd)
        # The following button takes 'switch_to_arrows' as a method. It calls this method when it's clicked.
        self.arrows = Button((screen_x/2)-100, screen_y-300, yellow, "SELECT: ARROW KEYS", "instructions_button", 200, 50, font_1, self.switch_to_arrows)
        self.back = Button((screen_x/2)-100, screen_y-200, yellow, "BACK", "back_button", 200, 50, font_1, self.switch_main_menu)
        self.current_selection = Textbox((screen_x/2)-175, screen_y-500, orange, "CURRENT SELECTION: " + str(self.share["current_controls"]), "current_selection", 350, 50, font_1)
        self.instructions_1 = Textbox(screen_x-325, screen_y-375, orange, "W/↑: MOVE UP", "current_selection", 200, 25, font_1)
        self.instructions_2 = Textbox(screen_x-325, screen_y-350, orange, "A/←:  MOVE LEFT", "current_selection", 200, 25, font_1)
        self.instructions_3 = Textbox(screen_x-325, screen_y-325, orange, "S/↓: MOVE DOWN", "current_selection", 200, 25, font_1)
        self.instructions_4 = Textbox(screen_x-325, screen_y-300, orange, "D/→: MOVE RIGHT", "current_selection", 200, 25, font_1)
        
    def cleanup(self):
        del self.title, self.wasd, self.arrows, self.back, self.current_selection

    def switch_to_wasd(self):
        """
        This modifies the value referenced by the key 'keys' in the share dictionary.
        This changes the controls to "WASD" to be used in the game.
        """
        self.share.update({"keys": [K_w, K_s, K_d, K_a]})
        self.share.update({"current_controls": "WASD"})
        del self.current_selection
        self.current_selection = Textbox((screen_x/2)-175, screen_y-500, orange, "CURRENT SELECTION: " + str(self.share["current_controls"]), "current_selection", 350, 50, font_1)
        menu_forward_sound.play()
        
    def switch_to_arrows(self):
        """
        This modifies the value referenced by the key 'keys' in the share dictionary.
        This changes the controls to the arrow keys to be used in the game.
        """
        self.share.update({"keys": [K_UP, K_DOWN, K_RIGHT, K_LEFT]})
        self.share.update({"current_controls": "ARROW KEYS"})
        del self.current_selection
        self.current_selection = Textbox((screen_x/2)-175, screen_y-500, orange, "CURRENT SELECTION: " + str(self.share["current_controls"]), "current_selection", 350, 50, font_1)
        menu_forward_sound.play()

    def switch_main_menu(self):
        self.next = "main_menu"
        menu_back_sound.play()
        self.running = False      

    def handle_events(self, event):
        self.wasd.check_clicked(event)
        self.arrows.check_clicked(event)
        self.back.check_clicked(event)

    def update(self):
        pass

    def render(self, screen):
        screen.fill(black)
        self.title.draw(screen)
        self.wasd.draw(screen)
        self.arrows.draw(screen)
        self.back.draw(screen)
        self.current_selection.draw(screen)
        self.instructions_1.draw(screen)
        self.instructions_2.draw(screen)
        self.instructions_3.draw(screen)
        self.instructions_4.draw(screen)
        


class Difficulty(States):
    def __init__(self):
        States.__init__(self)

    def setup(self):
        self.running = True
        self.title = Textbox((screen_x/2)-250, screen_y/9, red, "DIFFICULTY SELECT", "title_textbox", 500, 100, font_2)
        self.easy = Button((screen_x/2)-100, screen_y-500, yellow, "SELECT: EASY", "easy_button", 200, 50, font_1, self.switch_easy)
        self.medium = Button((screen_x/2)-100, screen_y-400, yellow, "SELECT: MEDIUM", "medium_button", 200, 50, font_1, self.switch_medium)
        self.hard = Button((screen_x/2)-100, screen_y-300, yellow, "SELECT: HARD", "hard_button", 200, 50, font_1, self.switch_hard)
        self.custom = Button((screen_x/2)-100, screen_y-200, yellow, "SELECT: CUSTOM", "custom_button", 200, 50, font_1, self.switch_custom_menu)
        self.back = Button((screen_x/2)-100, screen_y-100, yellow, "BACK", "back_button", 200, 50, font_1, self.switch_main_menu)

    def cleanup(self):
        del self.title, self.easy, self.medium, self.hard, self.back

    def handle_events(self, event):
        self.easy.check_clicked(event)
        self.medium.check_clicked(event)
        self.hard.check_clicked(event)
        self.custom.check_clicked(event)
        self.back.check_clicked(event)

    def switch_easy(self):
        """
        If 'easy' difficulty is selected, 'x_cells', 'y_cells' and 'timer' are modified accordingly.
        This is done in the 'share' dictionary, and is carried to the game state.
        """
        self.share.update({"x_cells": 20})
        self.share.update({"y_cells": 20})
        self.share.update({"timer": 15})
        self.share.update({"current_difficulty": "EASY"})
        self.next = "game"
        menu_forward_sound.play()
        self.running = False

    def switch_medium(self):
        """
        If 'medium' difficulty is selected, 'x_cells', 'y_cells' and 'timer' are modified accordingly.
        This is done in the 'share' dictionary, and is carried to the game state.
        """
        self.share.update({"x_cells": 35})
        self.share.update({"y_cells": 35})
        self.share.update({"timer": 10})
        self.share.update({"current_difficulty": "MEDIUM"})
        self.next = "game"
        menu_forward_sound.play()
        self.running = False

    def switch_hard(self):
        """
        If 'hard' difficulty is selected, 'x_cells', 'y_cells' and 'timer' are modified accordingly.
        This is done in the 'share' dictionary, and is carried to the game state.
        """
        self.share.update({"x_cells": 50})
        self.share.update({"y_cells": 50})
        self.share.update({"timer": 5})
        self.share.update({"current_difficulty": "HARD"})
        self.next = "game"
        menu_forward_sound.play()
        self.running = False
    
    def switch_custom_menu(self):
        """
        If 'custom' difficulty is selected, the custom menu needs to be loaded.
        """
        self.next = "custom_menu"
        menu_forward_sound.play()
        self.running = False
    
    def switch_main_menu(self):
        self.next = "main_menu"
        menu_back_sound.play()
        self.running = False  
        
    def update(self):
        pass

    def render(self, screen):
        screen.fill(black)
        self.title.draw(screen)
        self.easy.draw(screen)
        self.medium.draw(screen)
        self.hard.draw(screen)
        self.custom.draw(screen)
        self.back.draw(screen)

class Custom_Menu(States):
    def __init__(self):
        States.__init__(self) # Initialises via the constructor of the superclass.
       
    def setup(self):
        self.running = True
        self.title = Textbox((screen_x/2)-250, screen_y/9, red, "CUSTOM GAME", "custom_title", 500, 100, font_2)
        self.instructions = Textbox((screen_x/2)-450, screen_y - 500, orange,
                                    "SELECT YOUR MAZE WIDTH/HEIGHT AND TIMER DURATION. ONLY SQUARE MAZES ARE SUPPORTED.",
                                    "instructions_textbox", 900, 50, font_1)
        self.size_textbox = Textbox((screen_x/2)-100, screen_y-400, orange, "WIDTH/HEIGHT: " + str(self.share["x_cells"]), "size_textbox", 200, 50, font_1)
        self.duration_textbox = Textbox((screen_x/2)-100, screen_y-300, orange, "DURATION: " + str(self.share["timer"]), "duration_textbox", 200, 50, font_1)
        self.back = Button((screen_x/2)-100, screen_y-100, yellow, "BACK", "back_button", 200, 50, font_1, self.switch_main_menu)
        self.size_increase = Button((screen_x/2)+110, screen_y-400, yellow, "+1", "back_button", 50, 50, font_1, self.increase_size)
        self.size_decrease = Button((screen_x/2)-160, screen_y-400, yellow, "-1", "back_button", 50, 50, font_1, self.decrease_size)
        self.duration_increase = Button((screen_x/2)+110, screen_y-300, yellow, "+1", "back_button", 50, 50, font_1, self.increase_duration)
        self.duration_decrease = Button((screen_x/2)-160, screen_y-300, yellow, "-1", "back_button", 50, 50, font_1, self.decrease_duration)
        self.play = Button((screen_x/2)-100, screen_y-200, yellow, "PLAY", "play_button", 200, 50, font_1, self.switch_game)
        
        
    def cleanup(self):
        del self.title, self.instructions, self.size_textbox, self.duration_textbox, self.back, self.size_increase, self.size_decrease, self.duration_increase, self.duration_decrease
    
    def handle_events(self, event):
        self.back.check_clicked(event)
        self.size_increase.check_clicked(event)
        self.size_decrease.check_clicked(event)
        self.duration_increase.check_clicked(event)
        self.duration_decrease.check_clicked(event)
        self.play.check_clicked(event)
    
    def increase_size(self):
        if (self.share["x_cells"] == 52) or (self.share["y_cells"] == 52):
            self.share.update({"x_cells": 1})
            self.share.update({"y_cells": 1})
            del self.size_textbox
            self.size_textbox = Textbox((screen_x/2)-100, screen_y-400, orange, "WIDTH/HEIGHT: " + str(self.share["x_cells"]), "size_textbox", 200, 50, font_1)
        else:
            self.share["x_cells"] = self.share["x_cells"] + 1
            self.share["y_cells"] = self.share["y_cells"] + 1
            del self.size_textbox
            self.size_textbox = Textbox((screen_x/2)-100, screen_y-400, orange, "WIDTH/HEIGHT: " + str(self.share["x_cells"]), "size_textbox", 200, 50, font_1)
    
    def decrease_size(self):
        if (self.share["x_cells"] == 1) or (self.share["y_cells"] == 1):
            self.share.update({"x_cells": 52})
            self.share.update({"y_cells": 52})
            del self.size_textbox
            self.size_textbox = Textbox((screen_x/2)-100, screen_y-400, orange, "WIDTH/HEIGHT: " + str(self.share["x_cells"]), "size_textbox", 200, 50, font_1)
        else:
            self.share["x_cells"] = self.share["x_cells"] - 1
            self.share["y_cells"] = self.share["y_cells"] - 1
            del self.size_textbox
            self.size_textbox = Textbox((screen_x/2)-100, screen_y-400, orange, "WIDTH/HEIGHT: " + str(self.share["x_cells"]), "size_textbox", 200, 50, font_1)
          
    def increase_duration(self):
        if (self.share["timer"] == 15):
            self.share.update({"timer": 1})
            del self.duration_textbox
            self.duration_textbox = Textbox((screen_x/2)-100, screen_y-300, orange, "DURATION: " + str(self.share["timer"]), "duration_textbox", 200, 50, font_1)
        else:
            self.share["timer"] = self.share["timer"] + 1
            del self.duration_textbox
            self.duration_textbox = Textbox((screen_x/2)-100, screen_y-300, orange, "DURATION: " + str(self.share["timer"]), "duration_textbox", 200, 50, font_1)
    
    def decrease_duration(self):
        if (self.share["timer"] == 1):
            self.share.update({"timer": 15})
            del self.duration_textbox
            self.duration_textbox = Textbox((screen_x/2)-100, screen_y-300, orange, "DURATION: " + str(self.share["timer"]), "duration_textbox", 200, 50, font_1)
        else:
            self.share["timer"] = self.share["timer"] - 1
            del self.duration_textbox
            self.duration_textbox = Textbox((screen_x/2)-100, screen_y-300, orange, "DURATION: " + str(self.share["timer"]), "duration_textbox", 200, 50, font_1)
    
    def switch_game(self):
        self.share.update({"current_difficulty": "CUSTOM"})
        self.next = "game"
        menu_forward_sound.play()
        self.running = False
    
    def switch_main_menu(self):
        self.next = "main_menu"
        menu_back_sound.play()
        self.running = False        
    
    def update(self):
        pass
       
    def render(self, screen):
        screen.fill(black)
        self.title.draw(screen)
        self.instructions.draw(screen)
        self.size_textbox.draw(screen)
        self.duration_textbox.draw(screen)
        self.back.draw(screen)
        self.size_increase.draw(screen)
        self.size_decrease.draw(screen)
        self.duration_increase.draw(screen)
        self.duration_decrease.draw(screen)
        self.play.draw(screen)
        

class Game(States):
    def __init__(self):
        States.__init__(self) # Initialises via the constructor of the superclass.

    def setup(self):
        self.running = True
        ### generates the maze and creates the walls
        """
        Uses the maze algorithm, passing in the width and height of the grid (x_cells and y_cells).
        """
        self.maze_data = generate_maze(self.share["x_cells"], self.share["y_cells"]) 
        for index, row in enumerate(self.maze_data):
            row = "|" + row[1:] + "|"
            self.maze_data[index] = row
        self.maze_data.insert(0, "|" * (self.share["y_cells"] + 2))
        self.maze_data.append("|" * (self.share["x_cells"] +  2))
        self.walls = []
        self.cell_size = 10
        self.maze_x = ((screen_x/2)-(self.cell_size*((self.share["x_cells"]+2)/2)))
        self.maze_y = ((screen_y/2)-(self.cell_size*((self.share["y_cells"]+2)/2)))

        for x, tiles in enumerate(self.maze_data):
            for y, tile in enumerate(tiles):
                if tile == "|":
                    wall = Wall(self.maze_x + (y*10), self.maze_y + (x*10), self.cell_size, white)
                    self.walls.append(wall)

        ### Finds the appropriate location for the character and goal
        if self.maze_data[1][1] == '|':
            if self.maze_data[1][2] == '|':
                if self.maze_data[2][1] == '|':
                    if self.maze_data[2][2] == '|':
                        self.next = "game"
                        self.running = False
                    else:
                        self.default_xpos = (((screen_x/2)-(self.cell_size*((self.share["x_cells"]+2)/2))) + self.cell_size) + self.cell_size
                        self.default_ypos = (((screen_y/2)-(self.cell_size*((self.share["y_cells"]+2)/2))) + self.cell_size) + self.cell_size
                else:
                    self.default_xpos = (((screen_x/2)-(self.cell_size*((self.share["x_cells"]+2)/2))) + self.cell_size)
                    self.default_ypos = (((screen_y/2)-(self.cell_size*((self.share["y_cells"]+2)/2))) + self.cell_size) + self.cell_size

            else:
                self.default_xpos = (((screen_x/2)-(self.cell_size*((self.share["x_cells"]+2)/2))) + self.cell_size) + self.cell_size
                self.default_ypos = (((screen_y/2)-(self.cell_size*((self.share["y_cells"]+2)/2))) + self.cell_size)
        else:
            self.default_xpos = (((screen_x/2)-(self.cell_size*((self.share["x_cells"]+2)/2))) + self.cell_size)
            self.default_ypos = (((screen_y/2)-(self.cell_size*((self.share["y_cells"]+2)/2))) + self.cell_size)
            
        if self.maze_data[self.share["x_cells"]][self.share["x_cells"]] == '|':
            if self.maze_data[self.share["x_cells"] - 1][self.share["y_cells"]] == '|':
                if self.maze_data[self.share["x_cells"]][self.share["y_cells"] - 1] == '|':
                    if self.maze_data[self.share["x_cells"] - 1][self.share["y_cells"] - 1] == '|':
                        self.next = "game"
                        self.running = False
                    else:
                        self.goal_xpos = (((screen_x/2)+(self.cell_size*((self.share["x_cells"]-2)/2))) - self.cell_size)
                        self.goal_ypos = (((screen_y/2)+(self.cell_size*((self.share["y_cells"]-2)/2))) - self.cell_size)
                else:
                    self.goal_xpos = ((screen_x/2)+(self.cell_size*((self.share["x_cells"]-2)/2)))
                    self.goal_ypos = (((screen_y/2)+(self.cell_size*((self.share["y_cells"]-2)/2))) - self.cell_size)
            else:
                self.goal_xpos = (((screen_x/2)+(self.cell_size*((self.share["x_cells"]-2)/2))) - self.cell_size)
                self.goal_ypos = ((screen_y/2)+(self.cell_size*((self.share["y_cells"]-2)/2)))
        else:
            self.goal_xpos = ((screen_x/2)+(self.cell_size*((self.share["x_cells"]-2)/2))) # Originally 350
            self.goal_ypos = ((screen_y/2)+(self.cell_size*((self.share["y_cells"]-2)/2))) # Originally 310

                     
        ### Instantiates character, timer, textbox, goal
        self.character = Character(self.default_xpos, self.default_ypos, self.cell_size, self.cell_size, green, self.share["keys"], self.cell_size)
        self.timer = Timer(screen_x - 130, 30, red, 10, 10, self.share["timer"])
        self.title_textbox = Textbox((screen_x/2)-100, (screen_y/25), white, str(self.share["current_difficulty"]) + ": " + str(self.share["x_cells"]) + " by " + str(self.share["y_cells"]), "test", 200, 50, font_1)
        self.goal = Goal(self.goal_xpos, self.goal_ypos, self.cell_size, yellow)
        self.lava_cells = []
        self.forfeit_button = Button(25, screen_y/25, yellow, "FORFEIT", "forfeit_button", 200, 50, font_1, self.forfeit)


    def cleanup(self):
        """
        Deletes all objects on screen, including walls and lava.
        """
        del self.character, self.title_textbox, self.timer, self.goal, self.forfeit_button
        for wall in self.walls:
            del wall
        for lava in self.lava_cells:
            del lava
    
    def handle_events(self, event):
        self.forfeit_button.check_clicked(event)
        
    
    def update(self):
        """
        The following two variables are used to keep track of the character location,
        and to check when the character moves.
        """
        self.character_x = self.character.x
        self.character_y = self.character.y
        
        self.character.move(self.walls, self.timer) # Allows the character to move.
        self.timer.countdown() # The timer counts down.
        
        if (self.character.x != self.character_x) or (self.character.y != self.character_y): # If the character has moved at all...
            lava_cell = Lava(self.character_x, self.character_y, self.cell_size, red) # Instantiate a lava cell at the character's previous location.
            self.lava_cells.append(lava_cell) # Append this cell to the array of lava cells.
        
        for lava in self.lava_cells: # For all the lava cells in the array...
            lava.check_touching(self.character, self.timer) # Check if the character is touching any of the cells.
            
        self.goal.check_touching(self.character, self.timer) # Check if the character has reached the goal.
        if self.timer.timer_expired == True: # If the timer has expired...
            self.character.die() # Kill the character.
            self.next = "game_over" # Set the next state to the game over screen.
            self.running = False # Move to the next state.

        if self.goal.win: # If the character wins...
            """
            The following 'if' statements check what difficulty the player was playing at.
            """
            if self.share["current_difficulty"] == "EASY":
                self.share["easy_wins"] = self.share["easy_wins"] + 1
            if self.share["current_difficulty"] == "MEDIUM":
                self.share["medium_wins"] = self.share["medium_wins"] + 1
            if self.share["current_difficulty"] == "HARD":
                self.share["hard_wins"] = self.share["hard_wins"] + 1
             
            self.next = "game_won" # Set the next state to the winning screen.
            self.running = False # Move to the next state.

    def forfeit(self):
        self.timer.duration = 0
        
    def render(self, screen):
        screen.fill(black)
        for wall in self.walls: # Draws all the walls to screen.
            wall.draw(screen)
        self.character.draw(screen)
        self.goal.draw(screen)
        self.timer.draw(screen)
        self.title_textbox.draw(screen)
        for lava in self.lava_cells: # Draws all the lava cells to screen.
            lava.draw(screen)
        self.forfeit_button.draw(screen)

        
class Game_Over(States):
    def __init__(self):
        States.__init__(self)

    def setup(self):
        time.sleep(1.5) # Delay is used to stop the state jumping immediately (from the game state).
        self.running = True
        self.you_lose = Textbox((screen_x/2)-250, screen_y/9, red, "GAME OVER", "title_textbox", 500, 100, font_2)
        self.retry = Button((screen_x/2)-100, screen_y-500, yellow, "RETRY", "retry_game", 200, 50, font_1, self.switch_game)
        self.change_difficulty = Button((screen_x/2)-100, screen_y-400, yellow, "CHANGE DIFFICULTY", "retry_game", 200, 50, font_1, self.switch_difficulty)
        self.main_menu = Button((screen_x/2)-100, screen_y-300, yellow, "RETURN TO MENU", "return_to_menu", 200, 50, font_1, self.switch_main_menu)
        self.quit_button = Button((screen_x/2)-100, screen_y-200, yellow, "QUIT", "quit_button", 200, 50, font_1, self.quit_game)

    def cleanup(self):
        del self.you_lose, self.main_menu, self.retry, self.change_difficulty, self.quit_button

    def handle_events(self, event):
        self.main_menu.check_clicked(event)
        self.retry.check_clicked(event)
        self.change_difficulty.check_clicked(event)
        self.quit_button.check_clicked(event)

    def switch_difficulty(self):
        self.next = "difficulty_select"
        menu_forward_sound.play()
        self.running = False

    def switch_game(self):
        self.next = "game"
        menu_forward_sound.play()
        self.running = False

    def switch_main_menu(self):
        self.next = "main_menu"
        menu_back_sound.play()
        self.running = False
        
    def quit_game(self):
        """
        Exits the game.
        """
        exit_sound.play()
        self.quit = True

    def update(self):
        pass

    def render(self, screen):
        screen.fill(black)
        self.you_lose.draw(screen)
        self.main_menu.draw(screen)
        self.change_difficulty.draw(screen)
        self.retry.draw(screen)
        self.quit_button.draw(screen)
  
class You_Win(States):
    def __init__(self):
        States.__init__(self)

    def setup(self):
        time.sleep(1.5)
        self.running = True
        self.you_win = Textbox((screen_x/2)-250, screen_y/9, red, "YOU WIN!", "title_textbox", 500, 100, font_2)
        self.retry = Button((screen_x/2)-100, screen_y-500, yellow, "RETRY", "retry_game", 200, 50, font_1, self.switch_game)
        self.change_difficulty = Button((screen_x/2)-100, screen_y-400, yellow, "CHANGE DIFFICULTY", "retry_game", 200, 50, font_1, self.switch_difficulty)
        self.main_menu = Button((screen_x/2)-100, screen_y-300, yellow, "RETURN TO MENU", "return_to_menu", 200, 50, font_1, self.switch_main_menu)
        self.quit_button = Button((screen_x/2)-100, screen_y-200, yellow, "QUIT", "quit_button", 200, 50, font_1, self.quit_game)

    def cleanup(self):
        del self.you_win, self.main_menu, self.retry, self.change_difficulty, self.quit_button

    def handle_events(self, event):
        self.main_menu.check_clicked(event)
        self.retry.check_clicked(event)
        self.change_difficulty.check_clicked(event)
        self.quit_button.check_clicked(event)

    def switch_difficulty(self):
        self.next = "difficulty_select"
        menu_forward_sound.play()
        self.running = False
    
    def switch_game(self):
        self.next = "game"
        menu_forward_sound.play()
        self.running = False

    def switch_main_menu(self):
        self.next = "main_menu"
        menu_back_sound.play()
        self.running = False  
       
    def quit_game(self):
        """
        Exits the game.
        """
        exit_sound.play()
        self.quit = True

    def update(self):
        pass

    def render(self, screen):
        screen.fill(black)
        self.you_win.draw(screen)
        self.main_menu.draw(screen)
        self.change_difficulty.draw(screen)
        self.retry.draw(screen)
        self.quit_button.draw(screen)
        

class Control: # This class controls the entire program, handling all the states.
    def __init__(self):
        self.screen = pygame.display.set_mode((screen_x, screen_y)) # Sets up the screen according to the resolution (from assets.py).
        self.clock = pygame.time.Clock() # Sets up the pygame clock.
        self.running = True # Starts running the current state.
        self.state_dict = None # Initialises the state dictionary as None.
        self.current_state = None # Initialises the current state as None.

    def setup(self, state_dict, start_state): # This takes in the state dictionary and the start state, as a starting point for the program.
        # 'start_state' represents the key for the instance of the state in 'state_dict'.
        self.state_dict = state_dict 
        self.current_state = self.state_dict[start_state] # Sets the current state to an instance of the start state, referencing the state dictionary.
        self.current_state.setup() # Calls the setup method for the current state, instantiating all objects needed.

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Checks if the [X] button has been pressed.
                self.running = False 
            self.current_state.handle_events(event)

        if not(self.current_state.running): # If the current state is no longer running...
            self.change_state() # ...move to the next state.

        if self.current_state.quit == True: 
            self.running = False # Quits the game.

    def change_state(self):
        new_state = self.current_state.next # Sets up the key for the new state, to reference in 'state_dict'.
        self.current_state.cleanup() # Deletes all objects from the current state.
        self.current_state = self.state_dict[new_state] # Sets the current state to the object referenced by the key 'new_state', from 'state_dict'.
        self.current_state.setup() # Sets up the new current state.

    def main_loop(self): # Acts as a game loop.
        while self.running:
            self.clock.tick(fps)
            self.handle_events()
            self.current_state.update()
            self.current_state.render(self.screen)
            pygame.display.flip() # Refreshes display.



pygame.init() # Initialises pygame.
app = Control() # Creates an instance of 'Control', named 'app'.
"""
Below is the state dictionary. 
It contains instances of all the states.
"""
state_dict = {
    "main_menu": Main_Menu(),
    "difficulty_select": Difficulty(),
    "instructions_screen": Instructions(),
    "controls_screen" : Controls_Setup(),
    "custom_menu": Custom_Menu(),
    "game" : Game(),
    "game_won": You_Win(),
    "game_over": Game_Over(),
    }
"""
Below calls the setup method for app (instance of Control), 
and passes in the state dictionary and the main menu as the starting state.
"""
app.setup(state_dict, "main_menu")
app.main_loop()
pygame.quit() # Quits pygame. Only happens when [X] is pressed.