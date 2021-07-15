import urwid


class GameOverScreen(urwid.LineBox):
    """Display a the game over screen"""

    def __init__(self):
        text = urwid.Filler(urwid.Text("GAME OVER your sus or sadness meter was too high", 'center'), 'middle')
        button_restart = urwid.Button("RESTART", self.__restart)
        button_quit = urwid.Button("QUIT", self.__quit)
        buttons = urwid.Filler(urwid.GridFlow([button_quit, button_restart], 11, 5, 1, 'center'))

        super().__init__(urwid.Pile([text, buttons]), title="GAME OVER")

    def __restart(self, button):
        self._emit('restart')

    def __quit(self, button):
        self._emit('quit')

    def keypress(self, size, key):
        """Handles Keypress to get to Help Screen"""
        key = super().keypress(size, key)
        if str(key).lower() == 'h':
            self._emit('help')


urwid.register_signal(GameOverScreen, ['restart', 'quit'])
