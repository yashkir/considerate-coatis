

class make_situation:
    """This class makes situations and writes them to a json"""

    def __init__(self, file):

        self.file = open(f'situations/{file}.json', "a")

    def start(self):
        """Starts here"""
        self.file.write('\n{')
        self.prompt()
        self.end()
        again = input('do you want to make another one?: ')
        if again == 'y':
            self.start()

    def prompt(self):
        """User writes prompt"""
        prompt = input("prompt: ")
        self.file.write(f'"prompt": "{prompt}", ')
        self.file.write('"options": [ ')
        self.add_response()

    def end(self):
        """Ends here"""
        self.file.write('},')

    def add_stats(self):
        """Adds stats"""
        print("called")
        self.file.write('"stats": {')
        social = input("social: ")
        self.file.write(f'"social": {social}, ')

        athletic = input("athletic: ")
        self.file.write(f'"athletic": {athletic}, ')

        academic = input("academic: ")
        self.file.write(f'"academic": {academic}')
        self.file.write('}')

    def add_response(self):
        """Adds response"""
        self.file.write("{")
        response = input('response: ')
        self.file.write(f'"response": "{response}", ')
        self.add_stats()
        self.file.write("}")
        again = input('another response?: ')
        if again == 'y':
            self.file.write(',')
            self.add_response()
        else:
            self.file.write(']')


if __name__ == "__main__":
    m = make_situation(input("filename: "))
    m.start()
