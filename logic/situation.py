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

    def get_option_response(self) -> str:
        """Returns the response for an option given its index"""
        o_list = []
        for x in range(len(self.options)):
            o_list.append(self.options[x]['response'])
        return o_list

    def get_option_stats(self, index) -> dict:
        """Returns the stats for an option given its index"""
        return self.options[index]['stats']
