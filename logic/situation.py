class Situation:
    """Situation class"""

    def __init__(self, prompt, options):
        self.prompt = prompt
        self.options = options

    def get_prompt(self) -> str:
        """Returns the situation's prompt"""
        return self.prompt

    def get_option_count(self) -> int:
        """Returns the number of options"""
        return len(self.options)

    def get_option_response(self, index) -> str:
        """Returns the response for an option given its index"""
        return self.options[index]['response']

    def get_option_stats(self, index) -> dict:
        """Returns the stats for an option given its index"""
        return self.options[index]['stats']
