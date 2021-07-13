import urwid


class HelpScreen(urwid.LineBox):
    """Displays a Help screen giving basic controls and information about the game"""

    def __init__(self, last_screen):
        text = urwid.Filler(urwid.Text('PLACEHOLDER', 'center'), 'middle')
        button_back = urwid.Button('help', self.__help)
        buttons = urwid.Filler(urwid.GridFlow([button_back], 10, 5, 1, 'center'))
        self.last_screen = last_screen
        super().__init__(urwid.Pile([text, buttons]))

    def __help(self, button):
        self._emit('help')
