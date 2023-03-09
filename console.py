#!/usr/bin/python3
"""console of the AirBnb clone website"""
import cmd
import readline
import models.base_model as Base
import json
import datetime
import py_func
from models import storage


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
                    all_list.append(str(v))
            except FileNotFoundError:
                pass
            print(all_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        if line == "":
            print("** class name missing **")
        else:
            upvar = line.split()

            if upvar[0] != 'BaseModel':
                print("** class doesn't exist **")
            elif len(upvar) < 2:
                print("** instance id missing **")
            elif upvar[0] == 'BaseModel':
                key = "{}.{}".format(upvar[0], upvar[1])
                if len(upvar) < 3:
                    print("** attribute name missing **")
                    return
                elif len(upvar) < 4:
                    print("** value missing **")
                else:
                    try:
                        with open('file.json', 'r') as f:
                            dicts_all = json.load(f)
                    except FileNotFoundError:
                        print("** no instance found **")
                        return
                    for k, v in dicts_all.items():
                        if k == key:
                            args = line.split()
                            d = storage.all()
                            for i in range(len(args[1:]) + 1):
                                if args[i][0] == '"':
                                    args[i] = args[i].replace('"', "")
                            key = upvar[0] + '.' + upvar[1]
                            attr_k = upvar[2]
                            attr_v = upvar[3]
                            try:
                                if attr_v.isdigit():
                                    attr_v = int(attr_v)
                                elif float(attr_v):
                                    attr_v = float(attr_v)
                            except ValueError:
                                pass
                            class_attr = type(d[key]).__dict__
                            if attr_k in class_attr.keys():
                                try:
                                    attr_v = type(class_attr[attr_k])(attr_v)
                                except Exception:
                                    print("Entered wrong value type")
                                    return
                            print(d[key])
                            print(type(d[key]))
                            """
                            setattr(d[key], attr_k, attr_v)
                            storage.save()
                            """

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
