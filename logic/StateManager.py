import json
import os

from logic.player import Player, Stats

INITIAL_STATE_PATH = os.path.join("logic", "initial_state.json")


class StateManager():
    """Exposes functionality for managing game state."""

    def __init__(self):
        self.state = {}
        self.player = Player(Stats(50, 50, 50, 50), 1, 1)

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
