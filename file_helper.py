#!/usr//bin/env python
# -*- coding:UTF-8 -*-

import os


def copy_override(source, destination):
    os.system('cp -f %s %s' % (source, destination))
    pass


def rename(new_name, path):
    old_name = path.spilt()
    os.system('rename ')
    pass


