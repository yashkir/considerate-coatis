import urwid

from logic.player import Player, Stats
from logic.StateManager import StateManager
from screens.game_screen import GameScreen
from screens.new_game_screen import NewGameScreen
from screens.restart_game_screen import RestartGameScreen
from screens.state_manager_screen import StateManagerScreen


class GameController():
    """Shows a new game prompt and switches to the game screen or quits."""

    def __init__(self):
        self.player = Player(Stats(50, 50, 50, 50), 1, 1)

        self.new_game_screen = NewGameScreen()
        self.restart_game_screen = RestartGameScreen()
        self.state_manager_screen = StateManagerScreen()
        self.game_screen = GameScreen(self.player)
        self.state_manager = StateManager()

        self.loop = urwid.MainLoop(self.new_game_screen)

        urwid.connect_signal(self.new_game_screen, 'start game', self.__start)
        urwid.connect_signal(self.new_game_screen, 'quit', self.__quit)
        urwid.connect_signal(self.new_game_screen, 'load', self.__show_state_manager_screen)

        urwid.connect_signal(self.restart_game_screen, 'restart', self.__restart)
        urwid.connect_signal(self.restart_game_screen, 'go back', self.__show_game_screen)
        urwid.connect_signal(self.restart_game_screen, 'quit', self.__quit)

        urwid.connect_signal(self.state_manager_screen, 'back', self.__show_new_game_screen)
        urwid.connect_signal(self.state_manager_screen, 'load save', self.__load_save)

        urwid.connect_signal(self.game_screen, 'quit', self.__quit)
        urwid.connect_signal(self.game_screen, 'restart', self.__show_restart_screen)

        self.loop.run()

    def __start(self, signal_emitter=None):
        self.state_manager.load_initial_state()
        self.__show_game_screen()

    def __quit(self, signal_emitter=None):
        raise urwid.ExitMainLoop()

    def __restart(self, signal_emitter=None):
        self.loop.widget = self.new_game_screen

    def __load_save(self, signal_emitter=None):
        self.state_manager.load_state(self.state_manager_screen.chosen_save)
        self.__show_game_screen()

    def __show_new_game_screen(self, signal_emitter=None):
        self.loop.widget = self.new_game_screen

    def __show_game_screen(self, signal_emitter=None):
        self.loop.widget = self.game_screen

    def __show_restart_screen(self, signal_emitter=None):
        self.loop.widget = self.restart_game_screen

    def __show_state_manager_screen(self, signal_emitter=None):
        self.loop.widget = self.state_manager_screen


if __name__ == "__main__":
    g = GameController()
    print(g.player.stats.charisma)
