import urwid


class HelpScreen(urwid.LineBox):
    """Displays a Help screen giving basic controls and information about the game"""

    def __init__(self):
        text = urwid.Filler(urwid.Text('PLACEHOLDER', 'center'), 'middle')
        button_back = urwid.Button('RETURN', self.__return)
        buttons = urwid.Filler(urwid.GridFlow([button_back], 10, 5, 1, 'center'))
        super().__init__(urwid.Pile([text, buttons]), title="HELP")

    def __return(self, button):
        self._emit('prev')

    def keypress(self, size, key):
        """Handle q for quitting"""
        key = super().keypress(size, key)
        if str(key).lower() == 'h':
            self._emit('prev')


urwid.register_signal(HelpScreen, ['prev'])
