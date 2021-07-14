import datetime


def debug(*args, sep=' ', end='\n'):
    """Logs text to a file for debugging."""
    timestamp = datetime.datetime.now().strftime("%d %b. %Y %H:%M:%S")

    text = ''
    for i, arg in enumerate(args):
        text += str(arg)
        if i < len(args)-1:
            text += sep
    text += end

    with open('devtools/debug_logs.txt', 'a') as file:
        file.write(f'[{timestamp}] {text}')


if __name__ == '__main__':
    pass
