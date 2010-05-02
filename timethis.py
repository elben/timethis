# -*- coding: utf-8 -*-
"""
    timethis
    ~~~~~

    A quick and dirty profiling tool.
    
    :copyright: (c) 2010 by Elben Shira.
    :license: MIT, see LICENSE
"""

import time

def timethis(target):
  # TODO: make this persistentable by checking type(target). If function,
  # assume that we don't want persistence. If a string, then it is a user
  # option.
  #
  # TODO: clean this up
  # TODO: comment it
  # TODO: make prints prettier (use format strings to limit decimal places)
  if type(target) == type(timethis): #TODO: a better way to chk if function
    def decorator(*args, **kwargs):
      start = time.time()
      r = target(*args, **kwargs)
      total = time.time() - start

      name, filename, linenum = info(target)
      print "%s:%d (%s) %f seconds" % (filename, linenum, name, total)

      return r
    return decorator
  elif type(target) == str and target == 'persist':
    # we want persistence
    runs = []
    def decorator(target):
      def wrapper(*args, **kwargs):
        start = time.time()
        r = target(*args, **kwargs)
        total = time.time() - start
        runs.append(total)

        # TODO: print number of runs we've done
        name, filename, linenum = info(target)
        print "%s:%d (%s) %f seconds (avg: %f over %d runs)" % (filename,
                linenum, name, total, sum(runs)/len(runs), len(runs))

        return r
      return wrapper
    return decorator

def info(target):
    co = target.__code__
    return (co.co_name, co.co_filename, co.co_firstlineno)

