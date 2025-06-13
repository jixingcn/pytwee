#!/usr/bin/env python
'''
Test the story
'''
# pylint: disable=broad-exception-caught
# pylint: disable=no-value-for-parameter
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import unittest

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
