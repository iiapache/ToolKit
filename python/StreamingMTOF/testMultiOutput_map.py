#!/usr/bin/python
#-*- coding: utf-8 -*-

########################################################################
#
# Copyright (c) 2016 Baidu.com, Inc. All Rights Reserved
#
########################################################################

import sys
reload(sys)
sys.setdefaultencoding("utf8")
import os

curPath = os.path.dirname(os.path.realpath(__file__))

def mapper():
    for line in sys.stdin:
        line = line.strip()
        print "{}".format(line)

if __name__ == "__main__":
    mapper()
