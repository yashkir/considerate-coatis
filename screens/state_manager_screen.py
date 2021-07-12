import pathlib

import urwid


class StateManagerScreen(urwid.LineBox):
    """The TUI for loading a save"""

    def __init__(self):
        text = urwid.Filler(urwid.Text("what save do you want to load?", 'center'), 'middle')
        self.saves = []
        self.save_buttons = []
        self.chosen_save = None
        button_no = urwid.Button("BACK", self.__go_back)
        for path in pathlib.Path("saves").iterdir():
            if path.is_file():
                self.saves.append(path)
                self.save_buttons.append(urwid.Button(str.split(path.name, '.')[0], self.__load_save))

        buttons_grid = urwid.GridFlow([button_no]+self.save_buttons, 10, 5, 1, 'center')
        buttons = urwid.Filler(buttons_grid)

        super().__init__(urwid.Pile([text, buttons]), title="load save")

    def __go_back(self, button):
        self._emit('back')

    def __load_save(self, button):
        for path in self.saves:
            if button.label == str.split(path.name, '.')[0]:
                self.chosen_save = self.saves[self.saves.index(path)]
        self._emit("load save")


urwid.register_signal(StateManagerScreen, ['back', 'load save'])
