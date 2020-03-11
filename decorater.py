# 2)write a decorator it should through an error while the input file is more than 2mb.

import os
def file_size_validation(fun):
    def wrapper():
        file_path = fun()
        b = os.path.getsize(file_path)
        if 1000000 <= b < 1000000000:
            if int(b/1000000)<=2:
                return "file size is bellow 2mb"
            else:
                return "file size more then 2 mb"
        else:
            return "file size bellow 2mb"
    return wrapper

@file_size_validation
def fun():
    file_name = "/home/fission/Desktop/sample.csv"
    return file_name
print(fun())
