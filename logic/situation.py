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
