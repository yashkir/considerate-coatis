import json
import os

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
        self.load_state(INITIAL_STATE_PATH)

    def save_state(self, path: str) -> None:
        """Save state to file."""
        file = open(path, mode='w')
        json.dump(self.state, file)
        file.close()

    def load_state(self, path: str) -> None:
        """Load state from file."""
        file = open(path, mode='r')
        self.state = json.load(file)
        self.game.situation_manager.load_situation(self.state[0]['situation_id'], specific=True)
        self.__set_state()
        file.close()

    def reset(self):
        """Reset everything"""
        self.game.situation_manager.reset()
        self.player_stats.reset()
        self.load_initial_state()
        self.game.game_screen.update_text()

    def __set_state(self):
        """Sets the player state to the state that is loaded"""
        self.player_stats.sus_int, self.player_stats.sad_int = 0, 0

        for stat, value in self.state[0]['player']['stats'].items():
            if value - 50 > 0:
                self.player_stats.sus_int += value - 50
            if value - 50 < 0:
                self.player_stats.sad_int += (value - 50) * -1
            self.player_stats.stat_dict[stat] = value

        self.player_stats.update_text()

    def apply_stats(self, response):
        """Apply the chosen option's stats to the player"""
        self.stats = self.game.situation_manager.current_situation.get_option_stats(int(response[0])-1)
        cur_stats = self.player_stats.stat_dict

        for stat, value in self.stats.items():
            # add the chosen option's stats
            cur_stats[stat] += self.stats[stat]
            self.state[0]['player']['stats'][stat] = self.player_stats.stat_dict[stat]

        for stat, value in self.state[0]['player']['stats'].items():
            if value > 50:
                self.player_stats.sus_int += value - 50
                self.player_stats.sad_int -= value - 50
            elif value < 50:
                self.player_stats.sad_int += (value - 50) * -1
                self.player_stats.sus_int -= (value - 50) * -1
            if self.player_stats.sad_int < 0:
                self.player_stats.sad_int = 0
            if self.player_stats.sus_int < 0:
                self.player_stats.sus_int = 0

        if self.player_stats.sus_int > 50 or self.player_stats.sad_int > 50:
            self.game.game_screen.game_over()

        if self.state[0]['situation_id'] == len(self.game.situation_manager.situations_cannon):
            self.game.game_screen.game_won()

        else:
            self.game.game_screen.situation_manager.load_situation(self.state[0]['situation_id'])
        if self.game.situation_manager.situation_counter == 5:
            self.state[0]['situation_id'] += 1

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
