import urwid


class GameScreen(urwid.LineBox):
    """Main game screen."""

    def __init__(self, player):
        self.text = urwid.Text("placeholder")
        self.fill = urwid.Filler(self.text, 'top')
        self.player = player
        self.stats_box = urwid.LineBox(urwid.Filler(self.player.stats.stat_list_text, 'middle'), title="stats")
        self.location_box = urwid.LineBox(self.fill, title="location")
        self.event_box = urwid.LineBox(self.fill, title="event")

        # buttons
        self.button_one = urwid.Button("quit", lambda _: self._emit('quit'))
        self.button_two = urwid.Button("Restart", lambda _: self._emit('restart'))
        self.button_columns = urwid.Columns([
            urwid.Filler(self.button_one, 'top'), urwid.Filler(self.button_two, 'top')])
        self.button_box = urwid.LineBox(self.button_columns, title="buttons")

        # Arrange a pile with two columns on top and events on bottom
        self.top_columns = urwid.Columns([('weight', 3.5, self.location_box), self.stats_box])
        self.pile = urwid.Pile([('weight', 3, self.top_columns), ('weight', 1.5, self.event_box), self.button_box])
        super().__init__(self.pile, title="Game Screen")

    def keypress(self, size, key):
        """Handle q for quitting"""
        key = super().keypress(size, key)
        if str(key).lower() == 'r':
            self.text.set_text("random")
            self.player.stats.charisma += 1
            self.player.stats.update_text()
        if str(key).lower() == 'q':
            raise urwid.ExitMainLoop()


urwid.register_signal(GameScreen, ['quit', 'restart'])
