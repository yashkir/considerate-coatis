import urwid


class Stats:
    """Stats class to store all the stats that the npc and player will have."""

    def __init__(self, athletic_ablity, charisma, wisdom, smartness):
        self.athletic_ability = athletic_ablity
        self.charisma = charisma
        self.wisdom = wisdom
        self.smartness = smartness
        self.stat_list = [self.athletic_ability, self.charisma, self.wisdom, self.smartness]
        self.stat_list_text = urwid.Text(
            "strength: " + str(self.athletic_ability)+'\n'
            "charisma: " + str(self.charisma)+'\n'
            "wisdom: " + str(self.wisdom) + '\n'
            "smartness: " + str(self.smartness) + '\n')
        self.stat_list_filler = urwid.Filler(self.stat_list_text, 'middle')

    def update_text(self):
        """This is where the text will update"""
        stat_list_text = (
            "strength: " + str(self.athletic_ability)+'\n'+"charisma: " + str(self.charisma) + '\n'
            + "wisdom: " + str(self.wisdom) + '\n' + "smartness: " + str(self.smartness) + '\n')
        self.stat_list_text.set_text(stat_list_text)
        return stat_list_text

    def reset(self):
        """Resets stats"""
        self.athletic_ability = 50
        self.charisma = 50
        self.wisdom = 50
        self.smartness = 50


class Player:
    """The player class"""

    def __init__(self, stats, x, y):
        self.stats = stats
        self.x = x
        self.y = y
        # self.stats_fill = urwid.Filler(self.stats.stat_list_text, 'top')
