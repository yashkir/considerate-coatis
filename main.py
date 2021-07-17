import urwid

from logic.SituationManager import SituationManager
from logic.StateManager import StateManager
from screens.difficulty_screen import DifficultyScreen
from screens.game_over_screen import GameOverScreen
from screens.game_screen import GameScreen
from screens.help_screen import HelpScreen
from screens.new_game_screen import NewGameScreen
from screens.restart_game_screen import RestartGameScreen
from screens.save_screen import SaveGameScreen
from screens.state_manager_screen import StateManagerScreen
from screens.win_screen import WinScreen
from settings import OVERLAY_HEIGHT, OVERLAY_WIDTH, PALETTE, PALETTE_COLORS


class GameController():
    """Shows a new game prompt and switches to the game screen or quits."""

    def __init__(self):
        self.new_game_screen = NewGameScreen()
        self.difficulty_screen = DifficultyScreen()
        self.restart_game_screen = RestartGameScreen()
        self.help_screen = HelpScreen()
        self.situation_manager = SituationManager()
        self.state_manager_screen = StateManagerScreen()
        self.state_manager = StateManager(self)
        self.game_screen = GameScreen(self.state_manager, self.situation_manager)
        self.game_over_screen = GameOverScreen()
        self.save_screen = SaveGameScreen()
        self.win_screen = WinScreen()
        self.state_manager.load_initial_state()

        urwid.connect_signal(self.new_game_screen, 'start game', self.__start)
        urwid.connect_signal(self.new_game_screen, 'quit', self.__quit)
        urwid.connect_signal(self.new_game_screen, 'load', self.__show_state_manager_screen)
        urwid.connect_signal(self.new_game_screen, 'help', self.__show_help_screen)

        urwid.connect_signal(self.difficulty_screen, 'quit', self.__quit)
        urwid.connect_signal(self.difficulty_screen, 'chosen difficulty', self.__set_difficulty)

        urwid.connect_signal(self.restart_game_screen, 'restart', self.__restart)
        urwid.connect_signal(self.restart_game_screen, 'go back', self.__show_game_screen)
        urwid.connect_signal(self.restart_game_screen, 'quit', self.__quit)
        urwid.connect_signal(self.restart_game_screen, 'help', self.__show_help_screen)

        urwid.connect_signal(self.game_over_screen, 'quit', self.__quit)
        urwid.connect_signal(self.game_over_screen, 'restart', self.__restart)

        urwid.connect_signal(self.state_manager_screen, 'back', self.__show_new_game_screen)
        urwid.connect_signal(self.state_manager_screen, 'load save', self.__load_save)

        urwid.connect_signal(self.game_screen, 'quit', self.__quit)
        urwid.connect_signal(self.game_screen, 'restart', self.__show_restart_screen)
        urwid.connect_signal(self.game_screen, 'help', self.__show_help_screen)
        urwid.connect_signal(self.game_screen, 'choice', self.__consequence)
        urwid.connect_signal(self.game_screen, 'save', self.__show_save_game_screen)
        urwid.connect_signal(self.game_screen, 'game over', self.__show_game_over_screen)
        urwid.connect_signal(self.game_screen, 'won', self.__show_win_screen)

        urwid.connect_signal(self.help_screen, 'prev', self.__show_prev_screen)

        urwid.connect_signal(self.save_screen, 'back', self.__show_game_screen)
        urwid.connect_signal(self.save_screen, 'save', self.__save)

        urwid.connect_signal(self.win_screen, 'quit', self.__quit)

        # Set up background and overlay
        self.background = urwid.AttrMap(urwid.SolidFill('.'), 'background')
        self.overlay = urwid.Overlay(self.new_game_screen, self.background,
                                     'center', OVERLAY_WIDTH, 'middle', OVERLAY_HEIGHT)

        # Start the MainLoop
        self.loop = urwid.MainLoop(self.overlay, PALETTE)
        self.loop.screen.set_terminal_properties(colors=PALETTE_COLORS)
        self.prev = self.loop.widget
        self.loop.run()

    # Game Flow Methods

    def __start(self, signal_emitter=None):
        self.__show_difficulty_screen()

    def __consequence(self, signal_emitter=None, choice=""):
        self.state_manager.apply_stats(choice)

    def __set_difficulty(self, signal_emitter=None, choice=""):
        self.state_manager.state[0]["difficulty"] = choice
        self.game_screen.update_buttons(self.situation_manager.current_situation.get_option_response())
        self.game_screen.update_text()
        self.__show_game_screen()

    def __quit(self, signal_emitter=None):
        raise urwid.ExitMainLoop()

    def __restart(self, signal_emitter=None):
        self.__show_new_game_screen()
        self.state_manager.reset()

    def __save(self, signal_emitter=None):
        self.state_manager.save_state(f'saves/{str(self.save_screen.file_edit.get_edit_text())}.json')
        self.state_manager_screen.update()
        self.__show_game_screen()

    def __load_save(self, signal_emitter=None, chosen_save=""):
        self.state_manager.load_state(chosen_save)
        self.__start()

    # Screen Switching Methods

    def __show_save_game_screen(self, signal_emitter=None):
        self.__set_overlay(self.save_screen)

    def __show_new_game_screen(self, signal_emitter=None):
        self.__set_overlay(self.new_game_screen)

    def __show_game_screen(self, signal_emitter=None):
        self.__set_overlay(self.game_screen)

    def __show_restart_screen(self, signal_emitter=None):
        self.__set_overlay(self.restart_game_screen)

    def __show_state_manager_screen(self, signal_emitter=None):
        self.__set_overlay(self.state_manager_screen)

    def __show_help_screen(self, signal_emitter=None):
        self.prev = self.__get_overlay_top()
        self.__set_overlay(self.help_screen)

    def __show_prev_screen(self, signal_emitter=None):
        self.__set_overlay(self.prev)

    def __show_game_over_screen(self, signal_emitter=None):
        self.__set_overlay(self.game_over_screen)

    def __show_win_screen(self, signal_emitter=None):
        self.__set_overlay(self.win_screen)

    def __show_difficulty_screen(self, signal_emitter=None):
        self.__set_overlay(self.difficulty_screen)

    # Overlay methods

    def __get_overlay_top(self):
        return self.overlay.contents[1][0].original_widget

    def __set_overlay(self, widget):
        """Replace the top widget of the main overlay"""
        widget_styled = urwid.AttrMap(widget, 'base')
        self.overlay = urwid.Overlay(widget_styled, self.background,
                                     'center', OVERLAY_WIDTH, 'middle', OVERLAY_HEIGHT)
        self.loop.widget = self.overlay


if __name__ == "__main__":
    g = GameController()
