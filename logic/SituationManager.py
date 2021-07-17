import json
import random

from logic.situation import Situation


class SituationManager():
    """SituationManager class"""

    def __init__(self):
        self.current_situation = None
        self.situation_counter = 0
        with open('situations/landmark.json', 'r') as file:
            self.situations_cannon = json.load(file)
        with open('situations/normal.json', 'r') as file:
            self.situations_normal = json.load(file)

    def load_situation(self, id, specific=False) -> None:
        """Loads a new situation"""
        random.seed()
        if specific:
            data = self.situations_cannon[id]
        # Get the data for a landmark situation
        elif self.situation_counter >= 5:
            self.situation_counter = 0
            data = self.situations_cannon[id]

        # Get the data for a normal situation
        else:
            data = self.situations_normal[random.randint(0, len(self.situations_normal)-1)]

        # Set the current situation to a new one
        self.current_situation = Situation(**data)
        self.situation_counter += 1

    def get_situation(self) -> Situation:
        """Returns the current situation"""
        return self.current_situation

    def reset(self):
        """Resets everything"""
        self.current_situation = None
        self.situation_counter = 0


if __name__ == "__main__":
    sm = SituationManager()
    sm.load_situation()

    sit = sm.get_situation()
    print(sit.get_prompt())
    print(sit.get_options())
