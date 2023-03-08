#!/usr/bin/python3

class testing():
    __privclasattr = "this is private"
    __privdict = {}

    def call_priv(self):
        print(type(self).__privclasattr)
    def dict_def(self, *args):
        for arg in args:
            type(self).__privdict.update({arg: "{}".format(1)})

        print(type(self).__privdict)

if __name__ == "__main__":
    inst = testing()
    inst.call_priv()
    inst.dict_def("amigo", "gringo")

    try:
        with open("filename", "r") as f:
            f.write("ola")
    except FileNotFoundError:
        raise
