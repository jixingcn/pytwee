'''
Twee 2
'''

from . import twee


class Parser(twee.Parser):
    '''
    Parser for twee 2
    '''

    def __init__(self, story):
        super().__init__(story)

    def __call__(self, line):
        '''
        Parse the source
        '''
        raise NotImplementedError(f'{self.__class__} not ready!')


class Unparser(twee.Unparser):
    def __init__(self, story):
        super().__init__(story)

    def __call__(self):
        #raise NotImplementedError(f'{self.__class__} not ready!')
        return None
