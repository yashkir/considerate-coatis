import curses

class game:

    def __init__(self) -> None:
        self.playing = False
        self.widgets = []
        self.screen = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self.screen.keypad(True)

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
        print(key)
        if key == "K_ESCAPE" or key == "q":
            curses.endwin()
            self.playing = False
    
    def render_game_screen(self) -> None:
        ...

g = game()
g.run()
