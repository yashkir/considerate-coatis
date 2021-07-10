import curses
from widgets import *

class game:

    def __init__(self) -> None:
        self.playing = False
        self.widgets = []
        self.screen = curses.initscr()
        curses.noecho()
        curses.cbreak()
        curses.curs_set(False)
        self.screen.keypad(True)
        self.height = self.screen.getmaxyx()[0]-1
        self.width = self.screen.getmaxyx()[1]-1

    def update(self):
        
        ...

    def run(self):
        self.playing = True
        while self.playing:
            self.render_game_screen()
            self.update()
            self.handle_input()
            
    
    def handle_input(self):
        key = self.screen.getkey()
        #print(key)
        if key == "ESCAPE" or key == "q":
            curses.endwin()
            self.playing = False
    
    def render_game_screen(self) -> None:
        self.height = self.screen.getmaxyx()[0]-1
        self.width = self.screen.getmaxyx()[1]-1
        draw_square(self.screen, 0, 0, self.width, self.height, "game")
        draw_square(self.screen, 2, 1, round(self.width-self.width/3-2), round(self.height-self.height/3-1), "screen")
        draw_square(self.screen, round(self.width-self.width/3)+1, 1, round(self.width/3)-3, round(self.height-self.height/3-1), "stats")
        draw_square(self.screen, 2, round(self.height-self.height/3), self.width-4, round(self.height/3-1), "Text")
        ...

g = game()
g.run()