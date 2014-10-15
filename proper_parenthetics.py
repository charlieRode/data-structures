#!/usr/bin/env python

def proper_parenthetics(string):
    count= 0
    for c in string:
        if c not in [u'(', u')']:
            string= string.replace(c, u'')
    while True:
        if u'()' in string:
            string= string.replace(u'()', u'', 1)
        else: break
    if string==u'': return 0
    elif string[0]==u')': return -1
    else: return 1


