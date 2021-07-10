import urwid

class game:

    def __init__(self) -> None:
        self.playing = False
        self.widgets = []
        #self.loop = urwid.MainLoop(self.widgets, unhandled_input=self.handle_input)

    def update(self):
        ...
    
    def run(self):
        self.playing = True
        while self.playing:
            self.render_game_screen()
            self.update()
            self.handle_input()
    
    def handle_input(self, key: str):
        if str(key).lower() == 'q':
            self.loop.stop()
            quit()
    
    def render_game_screen(self) -> None:
        """Display the main game screen"""
        text = urwid.Text("placeholder")
        fill = urwid.Filler(text, 'top')

        # The main boxes
        location_box = urwid.LineBox(fill, title="location")
        stats_box = urwid.LineBox(fill, title="stats")
        event_box = urwid.LineBox(fill, title="event")

        # Arrange a pile with two columns on top and events on bottom
        top_columns = urwid.Columns([location_box, stats_box])
        pile = urwid.Pile([top_columns, event_box])

        # Put everything on one box
        box = urwid.LineBox(pile, title="Game Screen")

        self.loop = urwid.MainLoop(box, unhandled_input=self.handle_input)

        self.loop.run()

g = game()
g.run()
