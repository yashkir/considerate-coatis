#!/usr/bin/env python3

import urwid

import game_screen


def render_new_game() -> None:
    """Display a New Game prompt with a y/n"""
    text = urwid.Text("Welcome, would you like to start a new game? y/n")
    fill = urwid.Filler(text, 'top')

    box = urwid.LineBox(fill, title="New Game")

    def handle_input(key: str) -> None:
        if key.lower() == 'y':
            text.set_text("TODO start a new game here")
            loop.stop()
            game_screen.render_game_screen()
        elif key.lower() == 'n':
            loop.stop()
            quit()

    loop = urwid.MainLoop(box, unhandled_input=handle_input)

    loop.run()


if __name__ == "__main__":
    render_new_game()
