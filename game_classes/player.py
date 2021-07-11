
class Stats:

    def __init__(self, athletic_ablity, charisma, wisdom, smartness):
        self.atletic_ability = athletic_ablity
        self.charisma = charisma
        self.wisdom = wisdom
        self.smartness = smartness
        self.stat_list = ["athletic ability: " + str(self.atletic_ability), "charisma: " + str(self.charisma), "wisdom: " + str(self.wisdom), "smartness: " + str(self.smartness)]

    def update_stats(self):
        self.stat_list = ["athletic ability: " + str(self.atletic_ability), "charisma: " + str(self.charisma), "wisdom: " + str(self.wisdom), "smartness: " + str(self.smartness)]

class Player:

    def __init__(self, stats, x, y, game):
        self.stats = stats
        self.x = x
        self.y = y
        self.game = game
    
    def draw_stats(self):
        self.stats.update_stats()
        screen = self.game.screen
        for y in range(len(self.stats.stat_list)):
            screen.addstr(self.game.stats_box_pos[0]+y*2+1, self.game.stats_box_pos[1]+1, str(self.stats.stat_list[y]))
            ...
        