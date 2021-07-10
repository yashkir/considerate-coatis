#!/usr/bin/env python3

import urwid


def render_game_screen() -> None:
    """Display the main game screen"""
    text = urwid.Text("Welcome, this is the game screen...")
    fill = urwid.Filler(text, 'top')

    box = urwid.LineBox(fill, title="Game Screen")

    def handle_input(key: str) -> None:
        if key.lower() == 'q':
            loop.stop()
            quit()

    loop = urwid.MainLoop(box, unhandled_input=handle_input)

    loop.run()


if __name__ == "__main__":
    render_game_screen()
