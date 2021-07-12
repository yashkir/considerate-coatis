import urwid

from screens.game_screen import GameScreen
from screens.new_game_screen import NewGameScreen
from screens.restart_game_screen import RestartGameScreen
from screens.state_manager_screen import StateManagerScreen


class GameController():
    """Shows a new game prompt and switches to the game screen or quits."""

    def __init__(self):
        self.new_game_screen = NewGameScreen()
        self.restart_game_screen = RestartGameScreen()
        self.state_manager_screen = StateManagerScreen()
        self.game_screen = GameScreen()

        self.loop = urwid.MainLoop(self.new_game_screen)
        urwid.connect_signal(self.new_game_screen, 'start game', self.__show_game_screen)
        urwid.connect_signal(self.new_game_screen, 'quit', self.__quit)
        urwid.connect_signal(self.new_game_screen, 'load', self.__show_state_manager_screen)

        urwid.connect_signal(self.restart_game_screen, 'restart', self.__restart)
        urwid.connect_signal(self.restart_game_screen, 'go back', self.__show_game_screen)
        urwid.connect_signal(self.restart_game_screen, 'quit', self.__quit)

        urwid.connect_signal(self.state_manager_screen, 'back', self.__show_new_game_screen)

        urwid.connect_signal(self.game_screen, 'quit', self.__quit)
        urwid.connect_signal(self.game_screen, 'restart', self.__show_restart_screen)

        self.loop.run()

    def __quit(self, object):
        raise urwid.ExitMainLoop()

    def __show_restart_screen(self, object):
        self.loop.widget = self.restart_game_screen

    def __restart(self, object):
        self.loop.widget = self.new_game_screen

    def __show_game_screen(self, object):
        self.loop.widget = self.game_screen

    def __show_state_manager_screen(self, object):
        self.loop.widget = self.state_manager_screen

    def __show_new_game_screen(self, object):
        self.loop.widget = self.new_game_screen

    def __load_save(self, object):
        ...


if __name__ == "__main__":
    GameController()
