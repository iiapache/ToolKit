#!/usr/bin/env python
# -*- coding: utf-8 -*-

##########################
#@Desc: mrjob wordcount sample
#@Author: Joe
#@Date: 2016/11/14
##########################


from mrjob.job import MRJob

class MRWordCounter(MRJob):
    def mapper(self, key, line):
        for word in line.split():
            yield word, 1
    def reducer(self, word, occurrences):
        yield word, sum(occurrences)

if __name__ == "__main__":
    MRWordCounter.run()
