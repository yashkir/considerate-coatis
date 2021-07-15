import urwid


class HelpScreen(urwid.LineBox):
    """Displays a Help screen giving basic controls and information about the game"""

    def __init__(self):
        title = urwid.Filler(urwid.Text(title_text, 'center'), 'top')
        description = urwid.Filler(urwid.Text(description_text, 'center'), 'top')
        controls = urwid.Filler(urwid.Text(controls_text, 'center'), 'top')
        stats = urwid.Filler(urwid.Text(stats_text, 'center'), 'top')

        button_back = urwid.Button('RETURN', self.__return)
        buttons = urwid.Filler(urwid.GridFlow([button_back], 10, 5, 1, 'center'))
        super().__init__(urwid.Pile([title, description, controls, stats, buttons]), title="HELP")

    def __return(self, button):
        self._emit('prev')

    def keypress(self, size, key):
        """Handle q for quitting"""
        key = super().keypress(size, key)
        if str(key).lower() == 'h':
            self._emit('prev')


title1 = "__      __           _    _        __ _        _____  _  _    _      \n" # noqa: CODE
title2 = "\ \    / / ___  _ _ | |__(_) _ _  / _` |      |_   _|(_)| |_ | | ___ \n" # noqa: CODE
title3 = " \ \/\/ / / _ \| '_|| / /| || ' \ \__. |        | |  | ||  _|| |/ -_)\n" # noqa: CODE
title4 = "  \_/\_/  \___/|_|  |_\_\|_||_||_||___/         |_|  |_| \__||_|\___|\n" # noqa: CODE

title_text = title1 + title2 + title3 + title4

description_text = """Welcome to the game of alien life. You play as Xanathar, an alien trying to navigate their way through high school.
Your objective is not to stand out, but to remain under the radar and while still being as happy as possible.

You'll be met with many challenges and situations, and it's your job to navigate them to the end without drawing too much attention to yourself!"""# noqa: CODE

controls_text = """CONTROLS:
You can navigate the menu using the arrow and enter keys. However, here are two keys that will work from anywhere:
Q = Quits the program without saving
H = Takes you back to this help screen."""

stats_text = """ You'll be given several statistics, visible in the upper right hand corner of the screen.
If your Sus or Sadness level go higher than 50, YOU LOSE.

GOOD LUCK!"""

urwid.register_signal(HelpScreen, ['prev'])
