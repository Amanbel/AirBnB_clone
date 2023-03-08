#!/usr/bin/python3
"""console of the AirBnb clone website"""
import cmd
import readline


class console(cmd.Cmd):
    """a sub class of the cmd.Cmd class
    used to aquire all the necissary methods
    to build a command interpreter"""

    prompt = "(hbnb) "

    def do_EOF(self, line=None):
        """the end of line method of Cmd"""
        return True

    def do_quit(self, line=None):
        """command to exit the interpreter"""
        return exit

    def emptyline(self, line=None):
        return


if __name__ == "__main__":
    console().cmdloop()
