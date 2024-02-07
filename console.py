#!/usr/bin/python3
import cmd
import sys
"""Define class HBNBCommand"""


class HBNBCommand(cmd.Cmd):
    """A class that represent the implementation of the console"""
    prompt = "(hbnb) "
    file = None
    cmd.use_rawinput = True

    def preloop(self):
        if sys.stdin.isatty():
            pass
        else:
            cmd.use_rawinput = False

    def emptyline(self):
        """A method called when the user enters an empty line"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exits the interpreter"""
        return True

    def process_command(self, command):
        """Runs a command"""
        self.onecmd(command)

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it and prints the id"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()