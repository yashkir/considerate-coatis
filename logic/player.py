import urwid


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
        self.stat_list_text = urwid.Text("")
        self.stat_list_filler = urwid.Filler(self.stat_list_text, 'middle')

    def update_text(self):
        """This is where the text will update"""
        self.stat_dict['wisdom'] = self.stat_dict['smartness'] + self.stat_dict['charisma'] - 50
        stat_list_text = ([
            (
                'base',
                f"strength:  {self.stat_dict['athletic ability']}\n"
                + f"charisma:  {self.stat_dict['charisma']}\n"
                + f"wisdom:    {self.stat_dict['wisdom']}\n"
                + f"smartness: {self.stat_dict['smartness']}\n"
                + "-------------------------------------\n"
            ), (
                ('warning' if self.sus_int >= 35 else 'base'),
                f"sus:       {str(self.sus_int)} \n"
            ), (
                ('warning' if self.sad_int >= 35 else 'base'),
                f"sadness:   {str(self.sad_int)} \n"
            )
        ])
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
