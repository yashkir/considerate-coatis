import json
import os

from devtools.debug import debug
from logic.player import Stats

INITIAL_STATE_PATH = os.path.join("logic", "initial_state.json")


class StateManager():
    """Exposes functionality for managing game state."""

    def __init__(self, game):
        self.state = {}
        self.player_stats = Stats(50, 50, 50, 50)
        self.game = game

    def load_initial_state(self):
        """Generate a initial state for a new game."""
        self.state = self.load_state(INITIAL_STATE_PATH)

    def save_state(self, path: str) -> None:
        """Save state to file."""
        file = open(path, mode='w')
        json.dump(self.state, file)
        file.close()

    def load_state(self, path: str) -> None:
        """Load state from file."""
        file = open(path, mode='r')
        self.state = json.load(file)
        debug(self.state)
        file.close()

    def reset(self):
        """Reset everything"""
        self.game.situation_manager.reset()
        self.player_stats.reset()
        self.load_initial_state()
        self.load_situation()
        self.game.game_screen.update_text()

    def set_state(self):
        """Sets the player state to the state that is loaded"""
        cur_stats = self.player_stats
        cur_stats.athletic_ability = self.state[0]['player']['stats']['athletic ability']
        cur_stats.charisma = self.state[0]['player']['stats']['charisma']
        cur_stats.smartness = self.state[0]['player']['stats']['smartness']
        cur_stats.wisdom = self.state[0]['player']['stats']['wisdom']
        for x in self.state[0]['player']['stats']:
            if self.state[0]['player']['stats'][str(x)]-50 > 0:
                self.player_stats.sus_int += self.state[0]['player']['stats'][str(x)] - 50
            if self.state[0]['player']['stats'][str(x)]-50 < 0:
                self.player_stats.sad_int += (self.state[0]['player']['stats'][str(x)] - 50) * -1
        self.player_stats.update_text()

    def apply_stats(self, response):
        """Where the stats will be applied"""
        # TODO still more pork to cut here

        self.stats = self.game.situation_manager.current_situation.get_option_stats(int(response[0])-1)
        cur_stats = self.player_stats
        cur_stats.athletic_ability += self.stats['athletic']
        cur_stats.charisma += self.stats['social']
        cur_stats.smartness += self.stats['academic']
        cur_stats.wisdom += self.stats['social'] + self.stats['academic']
        for x in self.stats:
            if self.stats[x] > 0:
                self.player_stats.sus_int += self.stats[x]
            if self.stats[x] < 0:
                self.player_stats.sad_int += self.stats[x] * -1
        if self.player_stats.sus_int > 50 or self.player_stats.sad_int > 50:
            self.game.show_game_over_screen()
        else:
            self.game.game_screen.situation_manager.load_situation()
        self.game.game_screen.update_text()
        self.game.game_screen.update_buttons(self.game.situation_manager.current_situation.get_option_response())
        self.player_stats.update_text()


if __name__ == "__main__":

    print("Testing StateManager...")

    path = "test.json"

    manager_a = StateManager()
    manager_a.load_initial_state()
    manager_a.save_state(path)

    manager_b = StateManager()
    manager_b.load_state(path)

    if os.path.exists(path):
        os.remove(path)

    print("Saved state equals loaded state from same file: ")
    if manager_a.state == manager_b.state:
        print("\tPASSED")
    else:
        print("\tFAILED")
