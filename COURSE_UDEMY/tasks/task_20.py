"""Додати до класу методи, які реалізують це"""

import os
from pathlib import Path


class ThisPass:
    def __init__(self, path):
        self.CWD = os.getcwd()
        self.current = path or os.path.dirname(__file__)

    def parent(self):
        self.current = os.path.dirname(self.current)
        return self

    def get_path(self):
        return self.current

    def exists(self):
        return os.path.exists(self.current)

    def is_link(self):
        return os.path.islink(self.current)

    def depth(self):
        return len(self.current.split(os.sep))

    def create(self):
        os.makedirs(self.current)
        return self

    def __add__(self, obj):
        if not isinstance(obj, str):
            return NotImplemented
        return Path(os.path.join(self.current, obj))

    def get_path(self):
        return self.current

    def __str__(self):
        return self.current

    # def get_children(self, *, just_names=True):
    #     if just_names:
    #         return os.listdir(self.current)


path = ThisPass("C:\\Users\\nkv57\\Desktop\\COURSE_UDEMY_OOP")
path2 = path + "task"

print(path.current)
print(path2)
