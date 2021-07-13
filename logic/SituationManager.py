import json
import random

from situation import Situation


class SituationManager():
    """SituationManager class"""

    def __init__(self):
        self.current_situation = None
        self.situation_counter = 0

    def load_situation(self) -> None:
        """Loads a new situation"""
        random.seed()

        # Get the data for a landmark situation
        if self.situation_counter % 5 == 0:
            with open('situations/landmark.json', 'r') as file:
                situations = json.load(file)

            data = situations[self.situation_counter % 5]

        # Get the data for a normal situation
        else:
            with open('situations/normal.json', 'r') as file:
                situations = json.load(file)

            data = situations[random.randint(0, len(situations)-1)]

        # Set the current situation to a new one
        self.current_situation = Situation(**data)
        self.situation_counter += 1

    def get_situation(self) -> Situation:
        """Returns the current situation"""
        return self.current_situation


if __name__ == "__main__":
    sm = SituationManager()
    sm.load_situation()

    sit = sm.get_situation()
    print(sit.get_prompt())
    print(sit.get_options())
