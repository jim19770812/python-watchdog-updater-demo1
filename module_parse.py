import os
from os.path import splitext, basename


def parse_module_name(src_path)->str:
    temp = str(splitext(src_path)[0])
    temp=temp[2:] if temp.startswith("./") else temp
    result=".".join(temp.split(os.sep))
    return result


if __name__=="__main__":
    print()
    print(parse_module_name("./a.pyd"))
    print(parse_module_name("./commons/utils.py"))
    print(parse_module_name("./commons/files/fileutils.py"))