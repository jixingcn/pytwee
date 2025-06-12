'''
Story
'''

import json

class Header:
    def __init__(self, name, tags, metadata):
        if name is None:
            raise NameError('The header must have a name!')

        self.name = name

        self.tags = []
        if tags is not None:
            tags = tags.strip()
            if tags != '':
                tags = tags[1:-1]
                self.tags = tags.split(' ')

        self.metadata = {}
        if metadata is not None:
            self.metadata = json.loads(metadata)

    def __repr__(self):
        return f':: {self.name} {self.tags} {self.metadata}'

    @staticmethod
    def create(name, tags, metadata):
        if name is None:
            return None
        name = name.strip()
        if name == '':
            return None
        if tags is not None:
            tags = tags.strip()
        if metadata is not None:
            metadata = metadata.strip()
        return Header(name, tags, metadata)


class Passage:
    def __init__(self, header, context):
        self.header  = header
        self.context = context

    def __repr__(self):
        return f'{self.header}\n{self.context}'


class Story:
    '''
    Story
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
