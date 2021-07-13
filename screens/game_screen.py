import urwid


class GameScreen(urwid.LineBox):
    """Main game screen."""

    def __init__(self, player):
        self.text = urwid.Text("placeholder")
        self.fill = urwid.Filler(self.text, 'top')
        self.player = player

        # The main boxes
        self.stats_box = urwid.LineBox(self.player.stats.stat_list_text, title="stats")
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

        # Put everything on one box
        # box = urwid.LineBox(pile, title="Game Screen")
        super().__init__(self.pile, title="Game Screen")
        # self.update()

    def __update(self):
        """The update variable to update everything on the screen at will"""
        # The main boxes
        self.stats_box = urwid.LineBox(self.player.stats.stat_list_text, title="stats")
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

        # Put everything on one box
        # box = urwid.LineBox(pile, title="Game Screen")
        super().__init__(self.pile, title="Game Screen")

    def keypress(self, size, key):
        """Handle q for quitting"""
        key = super().keypress(size, key)
        if str(key).lower() == 'r':
            self.text.set_text("random")
            self.player.stats.charisma += 1
            self.player.stats.update_stats()
            self.__update()
        if str(key).lower() == 'q':
            raise urwid.ExitMainLoop()


urwid.register_signal(GameScreen, ['quit', 'restart'])
