import urwid


class DifficultyScreen(urwid.LineBox):
    """Where the difficulty is chosen"""

    def __init__(self):
        text = urwid.Filler(urwid.Text("What is the difficulty you want the game to be on?", 'center'), 'middle')

        button_easy = urwid.Button("EASY", self.__difficulty)
        button_hard = urwid.Button("HARD", self.__difficulty)
        button_quit = urwid.Button("QUIT", self.__quit)
        buttons = urwid.Filler(urwid.GridFlow([button_easy, button_hard, button_quit], 10, 5, 1, 'center'))

        super().__init__(urwid.Pile([text, buttons]), title="select difficulty")

    def __quit(self, button):
        self._emit('quit')

    def __difficulty(self, button):
        self._emit('chosen difficulty', button.get_label())

    def keypress(self, size, key):
        """Handles Keypress to get to Help Screen"""
        key = super().keypress(size, key)
        if str(key).lower() == 'h':
            self._emit('help')


urwid.register_signal(DifficultyScreen, ['chosen difficulty', 'quit'])
