
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
        self.file_list.append('\n{')
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
        self.file_list.append(f'"prompt": "{prompt}", ')
        self.file_list.append('"options": [ ')
        self.file.write(f'"prompt": "{prompt}", ')
        self.file.write('"options": [ ')
        self.add_response()

    def end(self):
        """Ends here"""
        self.file_list.append('},')
        self.file.write('},')

    def add_stats(self):
        """Adds stats"""
        self.file_list.append('"stats: {')
        self.file.write('"stats": {')
        social = input("social: ")
        self.file_list.append(f'"social": {social}, ')
        self.file.write(f'"social": {social}, ')

        athletic = input("athletic: ")
        self.file_list.append(f'"athletic": {athletic}, ')
        self.file.write(f'"athletic": {athletic}, ')

        academic = input("academic: ")
        self.file_list.append(f'"academic": {academic}')
        self.file.write(f'"academic": {academic}')
        self.file_list.append('}')
        self.file.write('}')

    def add_response(self):
        """Adds response"""
        self.file_list.append("{")
        self.file.write("{")
        response = input('response: ')
        self.file_list.append(f'"response": "{response}", ')
        self.file.write(f'"response": "{response}", ')
        self.add_stats()
        self.file_list.append("}")
        self.file.write("}")
        again = input('another response?: ')
        if again == 'y':
            self.file_list.append(',')
            self.file.write(',')
            self.add_response()
        else:
            self.file_list.append(']')
            self.file.write(']')


if __name__ == "__main__":
    m = make_situation(input("filename: "))
