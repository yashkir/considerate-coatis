import urwid


class GameScreen(urwid.LineBox):
    """Main game screen."""

    def __init__(self):
        self.text = urwid.Text("placeholder")
        fill = urwid.Filler(self.text, 'top')

        # The main boxes
        location_box = urwid.LineBox(fill, title="location")
        stats_box = urwid.LineBox(fill, title="stats")
        event_box = urwid.LineBox(fill, title="event")

        # buttons
        button_one = urwid.Button("quit", lambda _: self._emit('quit'))
        button_two = urwid.Button("test button")
        button_columns = urwid.Columns([urwid.Filler(button_one, 'top'), urwid.Filler(button_two, 'top')])
        button_box = urwid.LineBox(button_columns, title="buttons")

        # Arrange a pile with two columns on top and events on bottom
        top_columns = urwid.Columns([location_box, stats_box])
        pile = urwid.Pile([button_box, top_columns, event_box])

        # Put everything on one box
        # box = urwid.LineBox(pile, title="Game Screen")
        super().__init__(pile, title="Game Screen")

    def keypress(self, size, key):
        """Handle q for quitting"""
        key = super().keypress(size, key)
        if str(key).lower() == 'r':
            self.text.set_text("random")
        if str(key).lower() == 'q':
            raise urwid.ExitMainLoop()


urwid.register_signal(GameScreen, ['quit'])