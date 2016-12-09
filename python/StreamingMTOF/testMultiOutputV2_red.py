#!/usr/bin/python
# -*- coding:utf-8 -*-

from operator import itemgetter
from itertools import groupby
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


def read_mapper_output(file, separator = '\t'):
    for line in file:
        yield line.rstrip().split(separator, 1)

def main(separator = '\t'):
    data = read_mapper_output(sys.stdin, separator = separator)
    for keyId, group in groupby(data, itemgetter(0)):
        try:
            for keyId, valueStr in group:
                pass
            num = int(keyId)
            if num <= 5:
                print "{}\t#A".format(keyId)
            else:
                print "{}\t#B".format(keyId)
        except ValueError:
            sys.stderr.write("reporter:counter:Reducer,ValueError,1\n")

if __name__ == "__main__":
    main()

