#!/usr/bin/env python
'''
A test
'''

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import pytwee # pylint: disable=wrong-import-position

if __name__ == '__main__':
    story = pytwee.story.Story()

    with open(os.path.join(os.path.dirname(__file__), 't001.tw'), 'rt', encoding='utf-8') as f:
        parser = pytwee.twee3.Parser(story)
        for line in iter(f.readline, ''):
            parser(line)
        del parser

    print('story:', story)

    twee2_unparser = pytwee.twee2.Unparser(story)
    print('---twee2_unparser')
    for line in iter(twee2_unparser, None):
        print(line)
