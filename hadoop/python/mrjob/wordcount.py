#!/usr/bin/env python
# -*- coding: utf-8 -*-

##########################
#@Desc: mrjob wordcount sample
#@Author: Joe
#@Date: 2016/11/14
##########################


from mrjob.job import MRJob
import re

WORD_RE = re.compile(r"[\w']+")

class MRWordCounter(MRJob):
    def mapper(self, key, line):
        # for word in line.split():
        for word in WORD_RE.findall(line):
            yield (word.lower(), 1)

    def combiner(self, word, occurrences):
        yield (word, sum(occurrences))

    def reducer(self, word, occurrences):
        yield (word, sum(occurrences))

if __name__ == "__main__":
    MRWordCounter.run()
