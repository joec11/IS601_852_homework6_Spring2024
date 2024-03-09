import logging
from app.commands import Command

class MenuCommand(Command):
    def execute(self, *args):
        logging.info("You entered the \'menu\' command.")
        print(f"You entered the \'menu\' command.")
