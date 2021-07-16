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
            urwid.Filler(self.state_manager.player_stats.stat_list_text, 'middle'), title="stats")
        self.location_box = urwid.LineBox(self.fill, title="location")
        self.situation_text = urwid.Text('none', align=CENTER)
        self.event_box = urwid.LineBox(urwid.Filler(self.situation_text, 'middle'), title="event")

        # buttons
        self.button_width = 20
        self.button_one = urwid.Button("quit", lambda _: self._emit('quit'))
        self.button_two = urwid.Button("Restart", lambda _: self._emit('restart'))
        self.button_three = urwid.Button("help", lambda _: self._emit('help'))
        self.button_four = urwid.Button("save", lambda _: self._emit('save'))
        self.button_columns = urwid.Filler(
            urwid.GridFlow(
                [self.button_one, self.button_two, self.button_three, self.button_four],
                self.button_width, 2, 1, 'center'))
        self.button_box = urwid.LineBox(self.button_columns, title="buttons")
        self.choice_count = 0

        # Arrange a pile with two columns on top and events on bottom
        self.top_columns = urwid.Columns([('weight', 1, self.location_box), self.stats_box])
        self.pile = urwid.Pile([
            ('weight', 1.5, self.top_columns), ('weight', 2, self.event_box), ('weight', 3, self.button_box)])
        super().__init__(self.pile, title="Game Screen")

    def game_over(self):
        """This is the call that the state manager makes when the game is over"""
        self._emit("game over")

    def game_won(self):
        """This is the call that the state manager makes when the game is won"""
        self._emit("won")

    def update_text(self):
        """Where all the text will be updated"""
        self.situation_text.set_text(self.situation_manager.current_situation.get_prompt())
        self.state_manager.player_stats.update_text()

    def update_buttons(self, response_list):
        """Where the buttons will be updated"""
        list_buttons = []

        list_buttons.append((self.button_one, ('given', 10)))
        list_buttons.append((self.button_two, ('given', 11)))
        list_buttons.append((self.button_three, ('given', 10)))
        list_buttons.append((self.button_four, ('given', 10)))

        for r in range(len(response_list)):
            list_buttons.append((
                urwid.Button(
                    str(r+1) + ' ' + str(response_list[r])
                    + self.situation_manager.current_situation.get_option_stats_str(r),
                    self.__choice), ('given', self.button_width)))

        self.button_columns.base_widget.contents = list_buttons

    def keypress(self, size, key):
        """Handle q for quitting and Keypress to get to Help Screen"""
        key = super().keypress(size, key)
        if str(key).lower() == 'q':
            raise urwid.ExitMainLoop()
        if str(key).lower() == 'h':
            self._emit('help')

    def __choice(self, object):
        self.button_columns.base_widget._w.focus.base_widget._set_focus_position(0)
        choice_text = object.get_label()
        self._emit('choice', choice_text)


urwid.register_signal(GameScreen, ['quit', 'restart', 'help', 'choice', 'save', 'game over', 'won'])
