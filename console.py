#!/usr/bin/python3
import cmd
import sys
import argparse
from copy import deepcopy
from models import storage
from models.base_model import BaseModel
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

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it and prints the id"""
        if len(arg) == 0:
            print("** class name missing **")
        else:
            try:
                obj = globals()[arg]
            except KeyError:
                print("** class doesn't exist **")
                return
            new = obj()
            new.save()
            print(new.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based
            on the class name and id"""
        parser = argparse.ArgumentParser()
        parser.add_argument('arguments', nargs='*')
        args = parser.parse_args(arg.split())
        if len(args.arguments) == 0:
            print("** class name missing **")
        elif len(args.arguments) == 1:
            print("** instance id missing **")
        else:
            try:
                obj = globals()[args.arguments[0]]
            except KeyError:
                print("** class doesn't exist **")
                return
            key = "{}.{}".format(args.arguments[0], args.arguments[1])
            objects = storage.all()
            for k in objects:
                if k == key:
                    print(objects[k])
                    return
            print("** no instance found **")

    def do_destroy(self, arg):
        """Prints the string representation of an instance based
            on the class name and id"""
        parser = argparse.ArgumentParser()
        parser.add_argument('arguments', nargs='*')
        args = parser.parse_args(arg.split())
        if len(args.arguments) == 0:
            print("** class name missing **")
        elif len(args.arguments) == 1:
            print("** instance id missing **")
        else:
            try:
                obj = globals()[args.arguments[0]]
            except KeyError:
                print("** class doesn't exist **")
                return
            key = "{}.{}".format(args.arguments[0], args.arguments[1])
            objects = storage.all()
            objects_copy = deepcopy(objects)
            flag = 0
            for k in objects_copy:
                if k == key:
                    del objects[k]
                    flag = 1
            if flag:
                for k in objects:
                    objects[k].save()
                return
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
