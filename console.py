#!/usr/bin/python3
"""console of the AirBnb clone website"""
import cmd
import readline
import models.base_model as Base
import models.user as Use
import models.city as city
import models.amenity as amenity
import models.review as review
import models.place as place
import models.state as state
import json
import datetime
import utils
from models import storage

dict_cls = {
        'BaseModel': Base.BaseModel,
        'User': Use.User,
        'City': city.City,
        'Amenity': amenity.Amenity,
        'Review': review.Review,
        'Place': place.Place,
        'State': state.State
        }


class HBNBCommand(cmd.Cmd):
    """a sub class of the cmd.Cmd class
    used to aquire all the necissary methods
    to build a command interpreter"""

    prompt = "(hbnb) "

    def precmd(self, line):
        """precommand is a funciton that processes lines given with
        the command before it reaches onecmd function"""
        if '.' in line:
            if 'all()' in line:
                al = line.split('.')
                return 'all {}'.format(al[0])
            d = {}
            try:
                with open('file.json', 'r') as f:
                    d = json.load(f)
            except FileNotFoundError:
                pass
            if "show" in line:
                al = line.split('.')
                alid = al[1].split("\"")
                for kd in d.keys():
                    k_d = kd.split('.')
                    if k_d[0] in line and 'show("{}")'.format(k_d[1]) in line:
                        return 'show {} {}'.format(k_d[0], k_d[1])
                return 'show {} {}'.format(al[0], alid[1])
            if "count()" in line:
                sp = line.split('.')
                count = 0
                for k in d.keys():
                    if sp[0] in k:
                        count = count + 1
                print(count)
                return ""
            if "destroy" in line:
                sp = line.split('.')
                spid = sp[1].split("\"")
                for kd in d.keys():
                    k_d = kd.split('.')
                    if (k_d[0] in line) and (k_d[1] in line):
                        return 'destroy {} {}'.format(k_d[0], k_d[1])
                return 'destroy {} {}'.format(sp[0], spid[1])
            if "update" in line:
                sp = line.split('.')
                sp2 = sp[1].split(' ')
                if "{" in line:
                    once = line.split(' ', 1)
                    id_list = once[0].split('"')
                    id_attr = id_list[1]
                    str_dict = once[1].split('{}')
                    in_dict = str_dict[0].replace(")", "")
                    for kd in d.keys():
                        k_d = kd.split('.')
                        if (sp[0] == k_d[0]) and (k_d[1] == id_attr):
                            return "update {} {} \
{}".format(k_d[0], k_d[1], in_dict)
                    return "update {} {} \
{}".format(sp[0], id_attr, in_dict)
                    # pass in the dictionary
                else:
                    args = sp2[1].split("\"")
                    args2 = sp2[2].split("\"")
                    attr1 = args[1]
                    attr2 = args2[1]
                    spid = sp2[0].split("\"")
                    id_attr = spid[1]
                    for kd in d.keys():
                        k_d = kd.split('.')
                        if (sp[0] == k_d[0]) and (k_d[1] == id_attr):
                            return "update {} {} {} \
{}".format(k_d[0], k_d[1], attr1, attr2)
                    return "update {} {} {} \
{}".format(sp[0], id_attr, attr1, attr2)

        else:
            return line

    def do_create(self, line):
        """command that creates an instance of the specified class
        and saves on to the file.json file"""
        if line == "":
            print("** class name missing **")

        elif line not in dict_cls.keys():
            print("** class doesn't exist **")
            return
        for k, v in dict_cls.items():
            if k == line:
                inst = v()
                inst.save()
                print(inst.id)
                break

    def do_show(self, line):
        """command that shows a specific data of a user or a subclass of
        BaseModel class, or BaseModel itself"""
        if line == "":
            print("** class name missing **")
            return

        cls_id = line.split()

        if cls_id[0] not in dict_cls.keys():
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
        """command that destorys a saved data on file.json"""
        if line == "":
            print("** class name missing **")
        else:
            cls_id = line.split()

            if cls_id[0] not in dict_cls.keys():
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
                    print("** no instance found **")

    def do_all(self, line):
        """shows all created instances of every class if there is no
        argument provided, if the a specific class is provided as an
        argument it shows all instances of that class"""
        if line in dict_cls.keys() or line == "":
            d = {}
            try:
                with open('file.json', 'r') as f:
                    d = json.load(f)
            except FileNotFoundError:
                pass
            if not line:
                print([str(x) for x in d.values()])
                return
            else:
                args = line.split()
                print([str(v) for k, v in d.items()
                    if args[0] in k])
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """command that updates a specific inctance of a class
        if the id is provided with the class name"""
        if line == "":
            print("** class name missing **")
        else:
            upvar = line.split()

            if upvar[0] not in dict_cls.keys():
                print("** class doesn't exist **")
            elif len(upvar) < 2:
                print("** instance id missing **")
            elif upvar[0] in dict_cls.keys():
                if len(upvar) < 3:
                    print("** attribute name missing **")
                    return
                elif len(upvar) < 4:
                    print("** value missing **")
                else:
                    key = "{}.{}".format(upvar[0], upvar[1])
                    try:
                        with open('file.json', 'r') as f:
                            dicts_all = json.load(f)
                    except FileNotFoundError:
                        print("** no instance found **")
                        return
                    for k, v in dicts_all.items():
                        if k == key:
                            d = storage.all()
                            args = line.split()
                            dict_chk = line.split(' ', 2)
                            for i in range(len(args[1:]) + 1):
                                if args[i][0] == '"':
                                    args[i] = args[i].replace('"', "")
                                elif args[i][0] == "'":
                                    args[i] = args[i].replace("'", "")
                            key = args[0] + '.' + args[1]
                            if dict_chk[2][0] == "{":
                                rep = dict_chk[2].replace("'", "\"")
                                to_dict = json.loads(rep)
                                """
                                for k, v in to_dict.items():
                                    to_dict[k] = utils.type_conv(v)
                                """
                                # update the dictionary input here
                            else:
                                attr_k = args[2]
                                attr_v = args[3]

                                attr_v = utils.type_conv(attr_v)
                                to_dict = {attr_k: attr_v}

                            spl = v.split(' ', 2)
                            dict_str = eval(spl[2])
                            
                            dump_dict = json.dumps(dict_str, default=utils.time_form)
                            load_dict = json.loads(dump_dict)
                            load_dict.update(to_dict)
                            
                            for ky, vl in dict_cls.items():
                                if upvar[0] == ky:
                                    inst = vl(**load_dict)

                            d[key] = str(inst)
                            with open('file.json', 'w') as f:
                                json.dump(d, f)
                            return
                    print("** no insatance found **")

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

