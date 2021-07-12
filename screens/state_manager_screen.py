import pathlib

import urwid


class StateManagerScreen(urwid.LineBox):
    """The TUI for loading a save"""

    def __init__(self):
        text = urwid.Filler(urwid.Text("what save do you want to load?", 'center'), 'middle')
        saves = []
        save_buttons = []
        button_no = urwid.Button("BACK", self.__go_back)
        for path in pathlib.Path("saves").iterdir():
            if path.is_file():
                saves.append(path)
                save_buttons.append(urwid.filler(urwid.Text(str.split(path.name, '.')[0]), 'center'), 'middle')
        buttons = urwid.Filler(urwid.GridFlow([button_no], 10, 5, 1, 'center'))

        super().__init__(urwid.Pile([text, buttons]), title="load save")

    def __go_back(self, button):
        self._emit('back')

    def __load_save(self, button):
        self._emit("load save")


urwid.register_signal(StateManagerScreen, ['back'])
