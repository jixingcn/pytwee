'''
Twee 3
'''

import re
import json
import uuid

from .story import Header, Passage
from . import twee


class StoryPassage:
    '''
    The common passage
    '''

    def __init__(self, story, header):
        if story is None:
            raise ValueError('The passage must have a story!')
        if header is None:
            raise ValueError('The passage must have a header!')

        self.story  = story
        self.header = header
        self.lines  = []

    def __call__(self, line):
        self.lines.append(line)

    def __del__(self):
        self.story.passages.append(Passage(self.header, '\n'.join(self.lines)))


class StoryTitle(StoryPassage):
    '''
    The special passage for the story title
    '''

    id = 'StoryTitle'

    def __init__(self, story, header):
        super().__init__(story, header)

        self.lines = []

    def __call__(self, line):
        self.lines.append(line)

    def __del__(self):
        self.story.title = self.header.name


class StoryData(StoryPassage):
    '''
    The special passage for the story data
    '''

    id = 'StoryData'

    def __init__(self, story, header):
        super().__init__(story, header)

        self.lines = []

    def __call__(self, line):
        self.lines.append(line)

    def __del__(self):
        data = json.loads('\n'.join(self.lines))

        if 'ifid' in data:
            data['ifid'] = uuid.UUID(data['ifid'])

        self.story.data = data


class Parser(twee.Parser):
    '''
    Parser for twee 3
    '''

    re_header = re.compile(r'''^([ \t]*::).*$''')
    re_header_detail = re.compile(r'\
^(?P<ntm>.*)(?P<ntm_t>\[.*\])[ \t]*(?P<ntm_m>\{.*\})[ \t]*\
|(?P<nmt>.*)(?P<nmt_m>\{.*\})[ \t]*(?P<nmt_t>\[.*\])[ \t]*\
|(?P<nt>.*)(?P<nt_t>\[.*\])[ \t]*\
|(?P<nm>.*)(?P<nm_m>\{.*\})[ \t]*\
|(?P<n>.*)$')

    def __init__(self, story):
        super().__init__(story)

        self.current = None

    def __call__(self, line): # pylint: disable=too-many-branches
        '''
        Parse the source
        '''
        rg_header = Parser.re_header.match(line)
        if rg_header is not None:
            rg_header = rg_header.groups()
            if len(rg_header) == 0:
                return
            rg_header = rg_header[0]

            rg_header = Parser.re_header_detail.match(line[len(rg_header):])
            if rg_header is None:
                return
            rg_header = rg_header.groupdict()

            header = None
            if rg_header['ntm'] is not None:
                header = Header.create(rg_header['ntm'], rg_header['ntm_t'], rg_header['ntm_m'])
            elif rg_header['nmt'] is not None:
                header = Header.create(rg_header['nmt'], rg_header['nmt_t'], rg_header['nmt_m'])
            elif rg_header['nt'] is not None:
                header = Header.create(rg_header['nt'], rg_header['nt_t'], None)
            elif rg_header['nm'] is not None:
                header = Header.create(rg_header['nm'], None, rg_header['nm_m'])
            elif rg_header['n'] is not None:
                header = Header.create(rg_header['n'], None, None)

            if header is None:
                return

            if header.name.startswith(StoryTitle.id):
                header.name  = header.name[len(StoryTitle.id):].strip()
                self.current = StoryTitle(self.story, header)
            elif header.name.startswith(StoryData.id):
                header.name  = header.name[len(StoryData.id):].strip()
                self.current = StoryData(self.story, header)
            else:
                self.current = StoryPassage(self.story, header)
        elif self.current is not None:
            self.current(line)

    def __del__(self):
        if self.current is not None:
            self.current = None


class Unparser(twee.Unparser): # pylint: disable=too-few-public-methods
    '''
    Unparser for twee 3
    '''
