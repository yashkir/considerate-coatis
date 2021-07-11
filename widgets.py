# `│ ─ ┌ ┬ ┐ ├ ┼ ┤ └ ┴ ┘`

def draw_square(screen, x, y, width, height, label):
    for wx in range(width):
        for hy in range(height):
            if wx == 0 and hy == 0:
                screen.addstr(y+hy, x+wx, "┌")
            elif wx == width-1 and hy == height-1:
                screen.addstr(y+hy, x+wx, "┘")
            elif wx == 0 and hy == height-1:
                screen.addstr(y+hy, x+wx, "└")
            elif wx == width-1 and hy == 0:
                screen.addstr(y+hy, x+wx, "┐")
            elif hy == 0:
                 screen.addstr(y+hy, x+wx, "─")
            elif wx == 0:
                screen.addstr(y+hy, x+wx, "│")
            elif hy == height-1:
                screen.addstr(y+hy, x+wx, "─")
            elif wx == width-1:
                screen.addstr(y+hy, x+wx, "│")
    
    width -= len(label)
    screen.addstr(y, round(width/2+x), label)
    ...