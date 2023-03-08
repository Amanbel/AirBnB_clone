#!/usr/bin/python3
"""console of the AirBnb clone website"""
import cmd
import readline
import models.base_model as Base
import json


class HBNBCommand(cmd.Cmd):
    """a sub class of the cmd.Cmd class
    used to aquire all the necissary methods
    to build a command interpreter"""

    prompt = "(hbnb) "

    def do_create(self, line):
        if line == "":
            print("** class name missing **")
        elif line != 'BaseModel':
            print("** class doesn't exist **")
        elif line == 'BaseModel':
            inst = Base.BaseModel()
            inst.save()
            print(inst.id)

    def do_show(self, line):
        if line == "":
            print("** class name missing **")
            return
        
        cls_id = line.split()

        if cls_id[0] != 'BaseModel':
            print("** class doesn't exist **")

        elif len(cls_id) != 2:
            print("** instance id missing **")

        else:
            key = "{}.{}".format(cls_id[0], cls_id[1])
            try:
                with open('file.json', 'r') as f:
                    dicts = json.load(f)
                for k, v in dicts.items():
                    if k == key:
                        print(v)
                        return
            except FileNotFoundError:
                pass
            print("** no instance found **")

    def do_destroy(self, line):
        if line == "":
            print("** class name missing **")
        else:
            cls_id = line.split()

            if cls_id[0] != 'BaseModel':
                print("** class doesn't exist **")
            elif len(cls_id) != 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(cls_id[0], cls_id[1])
                try:
                    with open('file.json', 'r') as f:
                        dict_all = json.load(f)
                except FileNotFoundError:
                    print("** no instance found **")
                    return
                if len(dict_all) == 0:
                    print("** no instance found **")
                else:
                    for k, v in dict_all.items():
                        if k == key:
                            dict_all.pop(key)
                            with open('file.json', 'w') as FILE:
                                json.dump(dict_all, FILE)
                            return

    def do_all(self, line):
        if line == 'BaseModel' or line == "":
            all_list = []
            try:
                with open('file.json', 'r') as f:
                    dicts_all = json.load(f)
                for k, v in dicts_all.items():
                    all_list.append(v)
            except FileNotFoundError:
                pass
            print(all_list)
        else:
            print("** class doesn't exist **")


    def do_EOF(self, line=None):
        """the end of line method of Cmd"""
        return True

    def do_quit(self, line=None):
        """Quit command to exit the program"""
        return exit

    def emptyline(self, line=None):
        return


if __name__ == "__main__":
    HBNBCommand().cmdloop()
