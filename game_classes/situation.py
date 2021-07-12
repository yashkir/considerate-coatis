import json


class Situation:
    """Situation class"""

    def __init__(self, prompt, options):
        self.prompt = prompt
        self.options = options

    def get_prompt(self) -> str:
        """Returns the situation's prompt"""
        return self.prompt

    def get_options(self) -> dict:
        """Returns the situation's options"""
        return self.options

    @classmethod
    def from_index(cls, index: int):
        """Returns a Situation object built from situations.json at index"""
        with open('situations.json', 'r') as file:
            data = json.load(file)

        situation = cls(**data[index])
        return situation
