from app.commands import Command

class GreetCommand(Command):
    def execute(self, *args):
        print(f'Hello! You entered the \'greet\' command.')
