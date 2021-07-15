import urwid


class SaveGameScreen(urwid.LineBox):
    """The screen where the user can save their progress"""

    def __init__(self):
        text = urwid.Filler(urwid.Text("Do you want to save?", 'center'), 'middle')
        self.file_edit = urwid.Edit(caption=u"filename: ")
        button_no = urwid.Button("NO", self.__back)
        button_done = urwid.Button("DONE", self.__save_to_file)
        buttons = urwid.Filler(urwid.GridFlow([button_no, self.file_edit, button_done], 10, 5, 1, 'center'))

        super().__init__(urwid.Pile([text, buttons]), title="Save Progress")

    def __back(self, button):
        self._emit('back')

    def __save_to_file(self, button):
        if not self.file_edit.get_edit_text:
            self.file_edit.set_edit_text('None')
        self._emit('save')

    def keypress(self, size, key):
        """Handles Keypress to get to Help Screen"""
        key = super().keypress(size, key)
        if str(key).lower() == 'h':
            self._emit('help')


urwid.register_signal(SaveGameScreen, ['back', 'save'])
