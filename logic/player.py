import urwid


class Stats:
    """Stats class to store all the stats that the npc and player will have."""

    def __init__(self, athletic_ablity, charisma, wisdom, smartness):
        self.athletic_ability = athletic_ablity
        self.charisma = charisma
        self.wisdom = wisdom
        self.smartness = smartness
        self.stat_list = [self.athletic_ability, self.charisma, self.wisdom, self.smartness]
        self.stat_list_text = [
            urwid.Text("strength: " + str(self.athletic_ability)),
            urwid.Text("charisma: " + str(self.charisma)),
            urwid.Text("wisdom: " + str(self.wisdom)), urwid.Text("smartness: " + str(self.smartness))]


class Player:
    """The player class"""

    def __init__(self, stats, x, y):
        self.stats = stats
        self.x = x
        self.y = y
        # self.stats_fill = urwid.Filler(self.stats.stat_list_text, 'top')

    def update_stats(self):
        """This is where the player's stats will be updated"""
        self.stats.stat_list_text = [
            urwid.Text("strength: " + str(self.stats.athletic_ability)),
            urwid.Text("charisma: " + str(self.stats.charisma)),
            urwid.Text("wisdom: " + str(self.stats.wisdom)), urwid.Text("smartness: " + str(self.stats.smartness))]
        ...
