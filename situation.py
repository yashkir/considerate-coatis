import json

class Situation:

    def __init__(self, prompt, options):
        self.prompt = prompt
        self.options = options

    def get_prompt(self) -> str:
        return self.prompt

    def get_options(self) -> dict:
        return self.options

    @classmethod
    def from_index(cls, index: int):

        with open('situations.json', 'r') as file:
            data = json.load(file)

        situation = cls(**data[index])
        return situation