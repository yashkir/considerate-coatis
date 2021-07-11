import urwid


class NewGameScreen(urwid.LineBox):
    """Display a New Game prompt, emit 'start game' on yes"""

    def __init__(self):
        text = urwid.Filler(urwid.Text("Welcome, would you like to start a new game?", 'center'), 'middle')
        button_yes = urwid.Button("YES", self.__start_game)
        button_no = urwid.Button("NO", self.__quit)
        buttons = urwid.Filler(urwid.GridFlow([button_yes, button_no], 10, 5, 1, 'center'))

        super().__init__(urwid.Pile([text, buttons]), title="New Game")

    def __start_game(self, button):
        self._emit('start game')

    def __quit(self, button):
        self._emit('quit')


urwid.register_signal(NewGameScreen, ['start game', 'quit'])