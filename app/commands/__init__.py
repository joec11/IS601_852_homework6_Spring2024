from abc import ABC, abstractmethod
from decimal import Decimal, InvalidOperation

class Command(ABC):
    @abstractmethod
    def execute(self): pass

class CommandHandler:
    def __init__(self): # Constructor
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        """Register Command"""
        self.commands[command_name] = command

    def execute_command(self, command_name: str):
        """Execute Command"""
        try:
            parts = command_name.split()
            assert 0 < len(parts) <= 3

            a_decimal, b_decimal = (map(Decimal, parts[:2]) if len(parts) > 2 else (Decimal(0.0), Decimal(1.0)))
            command = parts[-1]

            result = self.commands[command].execute(a_decimal, b_decimal)
            print(f"The result of {a_decimal} {command} {b_decimal} is equal to {result}") if (len(parts) > 2 and result is not None) else None
        except AssertionError:
            print("Usage: <number1> <number2> <operation/command> | <command>")
        except InvalidOperation:
            print("Invalid Operation")
        except KeyError:
            print(f"No such command: {command_name}")
        except ValueError as e:
            print(e)
