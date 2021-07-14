import urwid
from urwid.widget import CENTER


class GameScreen(urwid.LineBox):
    """Main game screen."""

    def __init__(self, state_manager, situation_manager):
        self.state_manager = state_manager
        self.situation_manager = situation_manager

        self.text = urwid.Text("placeholder")
        self.fill = urwid.Filler(self.text, 'top')
        self.stats_box = urwid.LineBox(
            urwid.Filler(self.state_manager.player.stats.stat_list_text, 'middle'), title="stats")
        self.location_box = urwid.LineBox(self.fill, title="location")
        self.situation_text = urwid.Text(self.situation_manager.current_situation.get_prompt(), align=CENTER)
        self.event_box = urwid.LineBox(urwid.Filler(self.situation_text, 'middle'), title="event")

        # buttons
        self.button_one = urwid.Button("quit", lambda _: self._emit('quit'))
        self.button_two = urwid.Button("Restart", lambda _: self._emit('restart'))
        self.button_columns = urwid.Columns([
            urwid.Filler(self.button_one, 'top'), urwid.Filler(self.button_two, 'top')])
        self.button_box = urwid.LineBox(self.button_columns, title="buttons")
        self.choice_count = 0

        # Arrange a pile with two columns on top and events on bottom
        self.top_columns = urwid.Columns([('weight', 1, self.location_box), self.stats_box])
        self.pile = urwid.Pile([('weight', 2, self.top_columns), ('weight', 1.5, self.event_box), self.button_box])
        super().__init__(self.pile, title="Game Screen")

    def update_text(self):
        """Where all the text will be updated"""
        self.situation_text.set_text(self.situation_manager.current_situation.get_prompt())
        self.state_manager.player.stats.update_text()

    def update_buttons(self, response_list):
        """Where the buttons will be updated"""
        list_buttons = []
        list_buttons.append((urwid.Filler(self.button_one, 'top'), ('weight', 1, False)))
        list_buttons.append((urwid.Filler(self.button_two, 'top'), ('weight', 1, False)))

        for r in range(len(response_list)):
            list_buttons.append((
                urwid.Filler(
                    urwid.Button(
                        str(r+1) + ' ' + str(response_list[r])
                        + self.situation_manager.current_situation.get_option_stats_str(r),
                        self.__choice), 'middle',), ('weight', 1, False)))

        final_buttons = urwid.MonitoredFocusList(list_buttons, focus=0)

        self.button_columns._set_contents(final_buttons)

    def __choice(self, object):
        choice_text = object.get_label()
        self._emit('choice', choice_text)


urwid.register_signal(GameScreen, ['quit', 'restart', 'choice'])
