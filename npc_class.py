# from player import Stats

class npc:

    def __init__(self, stats, x, y, game):
        self.stats = stats
        self.x = x
        self.y = y
        self.game = game
        self.screen = self.game.screen
    
    def say_prompt(self, x, y):
        prompt = " "
        # prompt = get_prompt()
        self.game.screen.addstr(y, x, prompt)

        