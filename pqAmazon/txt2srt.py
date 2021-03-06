# -*- coding: utf-8 -*-
# @Time    : 2021/4/18 下午3:58
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : txt2srt.py
# @Software: PyCharm
# !/usr/bin/python

import os
import sys
import re
from decimal import *
import glob

# fi = open(sys.argv[1], 'r')
#
# lines = fi.readlines()
#
# getcontext().prec = 7
#
# prefix = ""
# number = 1
# ifps = 25
# ofps = Decimal("23.976")
# ofps = 23

# if len(sys.argv) > 2:
#     ofps = Decimal(sys.argv[2])
#
# if len(sys.argv) > 3:
#     ifps = Decimal(sys.argv[3])


def toSeconds(c):
    global ofps
    fps = ofps
    c = c.strip("{}").strip("[]")
    c = Decimal(c) / fps
    ms = str(int((c % 1) * 1000))
    c = int(c)
    s = c % 60
    m = ((c - s) / 60) % 60
    h = (c - s - 60 * m) / 3600
    return str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2) + "," + str(ms).zfill(3)


def convert(line):
    global ifps
    global ofps
    chunks = re.split('({[0-9]+})', line)
    if (len(line) > 0) and (line[0] == '['):
        chunks = re.split('(\[[0-9]+\])', line)
        ofps = 10
    res = ""
    if len(chunks) == 5:
        fr = chunks[1]
        to = chunks[3]
        body = "\n".join(chunks[4].split("|"))
        res = toSeconds(fr) + " --> " + toSeconds(to) + "\n" + body.strip()
    else:
        s = re.match("[0-9]?[0-9]:([0-9][0-9]:){2}", line)
        if s != None:
            body = line[len(s.group()):]
            body = "\n".join(body.split("|"))
            s = s.group().zfill(9)
            c = int(s[0:2]) * 3600 * ifps + int(s[3:5]) * 60 * ifps + int(s[6:8]) * ifps
            res = toSeconds(str(c)) + " --> " + toSeconds(str(c + 5 * ifps)) + "\n" + body.strip()

    return res


if __name__ == '__main__':
    # global fi
    for file in glob.glob("/home/luolu/Desktop/amazontest/test/*.txt"):

        print(file)
        fi = open(file, 'r')

        lines = fi.readlines()

        getcontext().prec = 7

        prefix = file
        number = 1
        ifps = 25
        ofps = Decimal("23.976")

        for line in lines:
            print(prefix + str(number))
            number = number + 1
            prefix = "\n"
            oline = convert(line)
            print(oline)

        fi.close()




