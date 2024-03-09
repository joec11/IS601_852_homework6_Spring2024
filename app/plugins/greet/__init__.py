import logging
from app.commands import Command

class GreetCommand(Command):
    def execute(self, *args):
        logging.info("Hello! You entered the \'greet\' command.")
        print(f"Hello! You entered the \'greet\' command.")
