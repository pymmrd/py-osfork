#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""
  A fork that demostrates a copied environment
"""

import os
from os import environ

def my_fork():
    alist = [1, 2]
    environ['FOO'] = 'baz'
    print "FOO environmental variable set to: %s" % environ['FOO']
    environ['FOO'] = 'bar'
    print "FOO environmental variable set to: %s" % environ['FOO']
    child_pid = os.fork()
    if child_pid == 0:
        print id(alist), alist
        print "Child Process: PID# %s" % os.getpid()
        print "Child FOO environmental variable == %s" % environ['FOO']
    else:
        print id(alist), alist
        print "Parent Process: PID# %s" % os.getpid()
        print "Parent FOO environmental variable == %s" % environ['FOO']

if __name__ == "__main__":
    my_fork()


"""
子进程是父进程的副本，子进程获得父进程数据空间，堆和栈的副本。注意这是
子进程所拥有的副本。父，子进程并不共享这些存储空间.父，子进程共享正文段。
>>> my_fork()
FOO environmental variable set to: baz
FOO environmental variable set to: bar
140236106084296 [1, 2]
Parent Process: PID# 23047
Parent FOO environmental variable == bar
140236106084296 [1, 2]
Child Process: PID# 23048
Child FOO environmental variable == bar
"""

    
