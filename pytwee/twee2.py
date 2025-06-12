'''
Twee 2
'''

from . import twee


class Parser(twee.Parser): # pylint: disable=too-few-public-methods
    '''
    Parser for twee 2
    '''

    def __call__(self, line):
        '''
        Parse the source
        '''
        raise NotImplementedError(f'{self.__class__} not ready!')


class Unparser(twee.Unparser): # pylint: disable=too-few-public-methods
    '''
    Unparser for twee 2
    '''

    def __call__(self):
        #raise NotImplementedError(f'{self.__class__} not ready!')
        return None
