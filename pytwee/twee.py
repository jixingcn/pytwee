'''
Twee
'''
# pylint: disable=too-few-public-methods

class Parser:
    '''
    The parser interface
    '''

    def __init__(self, story):
        self.story = story


class Unparser:
    '''
    The unparser interface
    '''

    def __init__(self, story):
        self.story = story
