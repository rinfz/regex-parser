import re
import os


def decode_(func):
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        data = re.sub("\s*\/\/.*", "", data)
        data = re.sub("\/\*([\s\S]*?)\*\/", "", data)
        data = [d.lstrip() for d in data.split('\n')]
        data = [d.rstrip() for d in data]
        return ''.join(data)
    return wrapper

def get_file(filename):
    contents = None
    try:
        with open(filename, 'r') as handle:
            contents = ''.join(handle.readlines())
    except IOError as e:
        print e
    return contents

@decode_
def decode(string):
    if os.path.isfile(string):
        return get_file(string)
    return string
