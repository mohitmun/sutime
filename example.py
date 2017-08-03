import os
import json
from sutime import SUTime
import sys
# if __name__ == '__main__':
# test_case = u'I need a desk for today morning 11am'

jar_files = os.path.join(os.path.dirname(__file__), 'jars')
sutime = SUTime(jars=jar_files, mark_time_ranges=False)

# print(json.dumps(sutime.parse(test_case), sort_keys=True, indent=4))

def parse(s):
  return json.dumps(sutime.parse(s), sort_keys=True, indent=4) 
input = sys.argv[1:][0]
print("=====")
print(parse(input))
#     RubyPython.start
# sys = RubyPython.import("sys")
# sys.path.append('.')