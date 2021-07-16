import urwid
from urwid.widget import CENTER


class Stats:
    """Stats class to store all the stats that the npc and player will have."""

    def __init__(self, athletic_ablity, charisma, wisdom, smartness):
        self.athletic_ability = athletic_ablity
        self.charisma = charisma
        self.wisdom = wisdom
        self.smartness = smartness
        self.sus_int = 0
        self.sad_int = 0
        self.stat_dict = {
            "athletic ability": self.athletic_ability, "charisma": self.charisma,
            "wisdom": self.wisdom, "smartness": self.smartness}
        self.stat_list_text = urwid.Text(
            f"strength: {str(self.athletic_ability)}\ncharisma: {str(self.charisma)}\n"
            + f"wisdom: {str(self.wisdom)}\nsmartness: {str(self.smartness)}\n"
            + f"sus: {str(self.sus_int)}\nsadness: {str(self.sad_int)}\n", align=CENTER)
        self.stat_list_filler = urwid.Filler(self.stat_list_text, 'middle')

    def update_text(self):
        """This is where the text will update"""
        self.stat_dict['wisdom'] = self.stat_dict['smartness'] + self.stat_dict['charisma'] - 50
        stat_list_text = (
            f"strength: {self.stat_dict['athletic ability']}\ncharisma: {self.stat_dict['charisma']}\n"
            + f"wisdom: {self.stat_dict['wisdom']}\nsmartness: {self.stat_dict['smartness']}\n"
            + f"sus: {str(self.sus_int)}\nsadness: {str(self.sad_int)}\n")
        self.stat_list_text.set_text(stat_list_text)
        return stat_list_text

    def reset(self):
        """Resets stats"""
        self.athletic_ability = 50
        self.charisma = 50
        self.wisdom = 50
        self.smartness = 50
        self.sus_int = 0
        self.sad_int = 0
        self.stat_dict = {
            "athletic ability": self.athletic_ability, "charisma": self.charisma,
            "wisdom": self.wisdom, "smartness": self.smartness}
        self.update_text()
