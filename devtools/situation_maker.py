
class make_situation:
    """This class makes situations and writes them to a json"""

    def __init__(self, file):

        self.file_list = []
        self.file = open(f'situations/{file}.json', "a")
        self.filename = file
        self.start()

    def clean_up(self):
        """Cleans up everything nicely"""
        self.file.close()
        ...

    def start(self):
        """Starts here"""
        self.file.write('\n{')
        self.prompt()
        self.end()
        again = input('do you want to make another one?: ')
        if again == 'y':
            self.start()
        else:
            self.clean_up()

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
        self.file.write('"stats": {')
        charisma = input("charisma: ")
        self.file.write(f'"charisma": {charisma}, ')

        athletic_ablity = input("athletic ability: ")
        self.file.write(f'"athletic ability": {athletic_ablity}, ')

        smartness = input("smartness: ")
        self.file.write(f'"smartness": {smartness}')

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
