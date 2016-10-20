#!/usr/bin/env python
#coding: utf-8

"""
@Desc: 函数运行时间计时器,使用时在函数前面加上@fun_timer即可
@Author: Joe
@Date: 2016/10/19
"""
import time
import os
from functools import wraps

def fun_timer(function):
    @wraps(function)
    def function_timer(*args, **kwargs):
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        os.system("echo Total time running %s: %s seconds" %(function.func_name, str(t1-t0)) + " >> timecount.log")
        return result
    return function_timer

@fun_timer
def test():
    for i in range(0, 50):
        pass

if __name__ == "__main__":
    test()

