import urwid


class Stats:
    """Stats class to store all the stats that the npc and player will have."""

    def __init__(self, athletic_ablity, charisma, wisdom, smartness):
        self.atletic_ability = athletic_ablity
        self.charisma = charisma
        self.wisdom = wisdom
        self.smartness = smartness
        self.stat_list = [self.atletic_ability, self.charisma, self.wisdom, self.smartness]
        self.stat_list = [
            urwid.Text("athletic ability: " + str(self.atletic_ability)),
            urwid.Text("charisma: " + str(self.charisma)),
            urwid.Text("wisdom: " + str(self.wisdom)), urwid.Text("smartness: " + str(self.smartness))]


class Player:
    """The player class"""

    def __init__(self, stats, x, y, game):
        self.stats = stats
        self.x = x
        self.y = y

    def draw_stats(self):
        """This is where the player's stats will be drawn"""
        ...
