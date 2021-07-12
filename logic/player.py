
class Stats:
    """Stats class to store all the stats that the npc and player will have."""

    def __init__(self, athletic_ablity, charisma, wisdom, smartness):
        self.atletic_ability = athletic_ablity
        self.charisma = charisma
        self.wisdom = wisdom
        self.smartness = smartness
        self.stat_list = [
            "athletic ability: " + str(self.atletic_ability), "charisma: " + str(self.charisma),
            "wisdom: " + str(self.wisdom), "smartness: " + str(self.smartness)]

    def update_stats(self):
        """This will update the stats"""
        self.stat_list = [
            "athletic ability: " + str(self.atletic_ability), "charisma: " + str(self.charisma),
            "wisdom: " + str(self.wisdom), "smartness: " + str(self.smartness)]


class Player:
    """The player class"""

    def __init__(self, stats, x, y, game):
        self.stats = stats
        self.x = x
        self.y = y
        self.game = game
