#!/usr/bin/env python
'''
Test the story
'''
# pylint: disable=broad-exception-caught
# pylint: disable=no-value-for-parameter
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import unittest
import os

import pytwee


class TestHeaderMethods(unittest.TestCase):
    pass


class TestHeaderExceptions(unittest.TestCase):
    def test_without_name(self):
        try:
            pytwee.story.Header()
        except Exception as e:
            self.assertEqual(type(e), TypeError)

    def test_invalid_name(self):
        try:
            pytwee.story.Header(None)
        except Exception as e:
            self.assertEqual(type(e), ValueError)

    def test_invalid_tags(self):
        try:
            pytwee.story.Header('', tags=1)
        except Exception as e:
            self.assertEqual(type(e), TypeError)


class TestPassageMethods(unittest.TestCase):
    def test_parser(self):
        passage = pytwee.story.Passage(None, None)
        self.assertIsInstance(passage, pytwee.story.Passage)


class TestStoryMethods(unittest.TestCase):
    def test_parser(self):
        story = pytwee.Story()
        self.assertIsInstance(story, pytwee.Story)

        test_filepath = os.path.join(os.path.dirname(__file__), 't001.tw')
        with open(test_filepath, 'rt', encoding='utf-8') as f:
            parser = pytwee.twee3.Parser(story)
            for line in iter(f.readline, ''):
                parser(line)
            del parser # don't forget this line
