import urwid


class WinScreen(urwid.LineBox):
    """The win screen"""

    def __init__(self):
        text = urwid.Filler(urwid.Text(
             "____    ____  ______    __    __     ____    __    ____  __   __   __  \n" # noqa: CODE
            +"\   \  /   / /  __  \  |  |  |  |    \   \  /  \  /   / |  | |  \ |  | \n" # noqa: CODE
            +" \   \/   / |  |  |  | |  |  |  |     \   \/    \/   /  |  | |   \|  | \n" # noqa: CODE
            +"  \_    _/  |  |  |  | |  |  |  |      \            /   |  | |  . `  | \n" # noqa: CODE
            +"    |  |    |  `--'  | |  `--'  |       \    /\    /    |  | |  |\   | \n" # noqa: CODE
            +"    |__|     \______/   \______/         \__/  \__/     |__| |__| \__| \n", # noqa: CODE
             align='center'), 'middle')
        button_no = urwid.Button("accept your prize", self.__quit)
        buttons = urwid.Filler(urwid.GridFlow([button_no], 20, 5, 1, 'center'))

        super().__init__(urwid.Pile([text, buttons]), title="WINNER")

    def __quit(self, button):
        self._emit('quit')

    def keypress(self, size, key):
        """Handles Keypress to get to Help Screen"""
        key = super().keypress(size, key)
        if str(key).lower() == 'h':
            self._emit('help')


urwid.register_signal(WinScreen, ['quit'])
