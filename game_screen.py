#!/usr/bin/env python3

import urwid


def render_game_screen() -> None:
    """Display the main game screen"""
    text = urwid.Text("placeholder")
    fill = urwid.Filler(text, 'top')

    # The main boxes
    location_box = urwid.LineBox(fill, title="location")
    stats_box = urwid.LineBox(fill, title="stats")
    event_box = urwid.LineBox(fill, title="event")

    # Arrange a pile with two columns on top and events on bottom
    top_columns = urwid.Columns([location_box, stats_box])
    pile = urwid.Pile([top_columns, event_box])

    # Put everything on one box
    box = urwid.LineBox(pile, title="Game Screen")

    def handle_input(key: str) -> None:
        if str(key).lower() == 'q':
            loop.stop()
            quit()

    loop = urwid.MainLoop(box, unhandled_input=handle_input)

    loop.run()


if __name__ == "__main__":
    render_game_screen()
