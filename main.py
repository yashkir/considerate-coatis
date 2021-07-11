import urwid

from screens.game_screen import GameScreen
from screens.new_game_screen import NewGameScreen


class GameController():
    """Shows a new game prompt and switches to the game screen or quits."""

    def __init__(self):
        self.new_game_screen = NewGameScreen()
        self.loop = urwid.MainLoop(self.new_game_screen)

        urwid.connect_signal(self.new_game_screen, 'start game', self.__start_game)
        urwid.connect_signal(self.new_game_screen, 'quit', self.__quit)

        self.loop.run()

    def __start_game(self, object):
        """Replace the MainLoop widget with a new GameScreen"""
        self.game_screen = GameScreen()
        urwid.connect_signal(self.game_screen, 'quit', self.__quit)
        self.loop.widget = self.game_screen

    def __quit(self, object):
        raise urwid.ExitMainLoop()


if __name__ == "__main__":
    GameController()
