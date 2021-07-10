import curses

class game:

    def __init__(self) -> None:
        self.playing = False
        self.widgets = []

    def update(self):
        ...
    
    def run(self):
        self.playing = True
        while self.playing:
            self.render_game_screen()
            self.update()
            self.handle_input()
            
    
    def handle_input(self, key: str):
        ...
    
    def render_game_screen(self) -> None:
        ...

g = game()
g.run()
