#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Generate file(s) of specified size."""

import random


def _write(path, val):
    file = open(path, 'w')
    lst = [chr(c) for c in range(48, 58)+range(65, 91)+range(97, 123)]
    for i in xrange(int(val)):
        file.write(random.choice(lst).strip())
    file.close


with open('setting/path.conf', 'r') as fh:
    for line in fh:
        if line[0] == '#':
            continue

        path_val = line.strip().split("=")
        path = path_val[0]
        val = path_val[1]
        _write(path, val)
