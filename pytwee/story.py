'''
Story
'''

import json

class Header:
    '''
    The header of the passage
    '''

    def __init__(self, name, tags=None, metadata=None):
        if name is None:
            raise NameError('The header must have a name!')

        self.name = name

        self.tags = []
        if tags is not None:
            if isinstance(tags, str):
                tags = tags.strip()
                if tags != '':
                    tags = tags[1:-1]
                    self.tags = tags.split(' ')
            elif isinstance(tags, list):
                self.tags = tags
            else:
                raise ValueError('Input `tags` is not string or list!')

        self.metadata = {}
        if metadata is not None:
            if isinstance(metadata, str):
                self.metadata = json.loads(metadata)
            elif isinstance(metadata, map):
                self.metadata = json.loads(metadata)
            else:
                raise ValueError('Input `metadata` is not string or map!')

    def __repr__(self):
        return f':: {self.name} {self.tags} {self.metadata}'

    @staticmethod
    def create(name, tags=None, metadata=None):
        '''
        Create the header by name, tags, and metadata
        '''

        # Check the name
        if name is None:
            return None
        name = name.strip()
        if name == '':
            return None

        if tags is not None:
            tags = tags.strip()

        if metadata is not None:
            metadata = metadata.strip()

        return Header(name, tags=tags, metadata=metadata)


class Passage: # pylint: disable=too-few-public-methods
    '''
    The passage of the story
    '''

    def __init__(self, header, context):
        self.header  = header
        self.context = context

    def __repr__(self):
        return f'{self.header}\n{self.context}'


class Story: # pylint: disable=too-few-public-methods
    '''
    Story for the twine
    '''

    def __init__(self):
        self.title = None
        self.data  = {
            'ifid'          : None,
            'format'        : None,
            'format-version': None,
            'start'         : None,
            'tag-colors'    : None,
            'zoom'          : None,
        }
        self.passages = []

    def __repr__(self):
        return f'{self.title}\n{self.data}\n{self.passages}'
