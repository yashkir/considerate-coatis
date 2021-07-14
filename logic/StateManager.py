import json
import os

from logic.player import Player, Stats

INITIAL_STATE_PATH = os.path.join("logic", "initial_state.json")


class StateManager():
    """Exposes functionality for managing game state."""

    def __init__(self, game):
        self.state = {}
        self.player = Player(Stats(50, 50, 50, 50), 1, 1)
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
        file.close()

    def reset(self):
        """Reset everything"""
        self.game.situation_manager.reset()
        self.player.stats.reset()
        self.game.state_manager.load_initial_state()
        self.game.situation_manager.load_situation()
        self.game.game_screen.update_text()

    def set_state(self):
        """Sets the player state to the state that is loaded"""
        cur_stats = self.player.stats
        cur_stats.athletic_ability = self.state[0]['player']['stats']['athletic ability']
        cur_stats.charisma = self.state[0]['player']['stats']['charisma']
        cur_stats.smartness = self.state[0]['player']['stats']['smartness']
        cur_stats.wisdom = self.state[0]['player']['stats']['wisdom']
        self.player.stats.update_text()

    def apply_stats(self, response):
        """Where the stats will be applied"""
        # TODO still more pork to cut here
        responses = self.game.situation_manager.current_situation.get_option_response()
        for r in range(len(responses)):
            if response == responses[r]:
                chosen_response = r

        self.stats = self.game.situation_manager.current_situation.get_option_stats(chosen_response)
        cur_stats = self.player.stats
        cur_stats.athletic_ability += self.stats['athletic']
        cur_stats.charisma += self.stats['social']
        cur_stats.smartness += self.stats['academic']
        cur_stats.wisdom += self.stats['social'] + self.stats['academic']
        self.game.game_screen.situation_manager.load_situation()
        self.game.game_screen.update_text()
        self.game.game_screen.update_buttons(self.game.situation_manager.current_situation.get_option_response())
        self.player.stats.update_text()


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
