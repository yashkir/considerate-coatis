import urwid


class RestartGameScreen(urwid.LineBox):
    """Lets you restart the game."""

    def __init__(self):
        text = urwid.Filler(urwid.Text("Do you want to restart?", 'center'), 'middle')
        button_yes = urwid.Button("YES", self.__restart)
        button_no = urwid.Button("NO", self.__go_back)
        button_quit = urwid.Button("QUIT", self.__quit)
        buttons = urwid.Filler(urwid.GridFlow([button_yes, button_no, button_quit], 10, 5, 1, 'center'))

        super().__init__(urwid.Pile([text, buttons]), title="Restart game")

    def __restart(self, button):
        self._emit('restart')

    def __go_back(self, button):
        self._emit('go back')

    def __quit(self, button):
        self._emit('quit')


urwid.register_signal(RestartGameScreen, ['restart', 'go back', 'quit'])
