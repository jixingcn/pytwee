'''
Twee
'''

class Parser: # pylint: disable=too-few-public-methods
    '''
    The parser interface
    '''

    def __init__(self, story):
        self.story = story


class Unparser: # pylint: disable=too-few-public-methods
    '''
    The unparser interface
    '''

    def __init__(self, story):
        self.story = story
