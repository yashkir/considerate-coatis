
class npc:

    def __init__(self, charisma, strength, wisdom, smartness, x, y, game):
        self.charisma = charisma
        self.strength = strength
        self.wisdom = wisdom
        self.smartness = smartness
        self.x = x
        self.y = y
        self.game = game
        self.screen = self.game.screen
    
    def say_prompt(self, x, y):
        prompt = " "
        # prompt = get_prompt()
        self.game.screen.addstr(y, x, prompt)
        