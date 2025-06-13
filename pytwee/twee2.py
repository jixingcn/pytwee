'''
Twee 2
'''
# pylint: disable=too-few-public-methods

import uuid

from . import twee


class Parser(twee.Parser):
    '''
    Parser for twee 2
    '''

    def __call__(self, line):
        '''
        Parse the source
        '''
        raise NotImplementedError(f'{self.__class__} not ready!')


class UnparserHTML(twee.Unparser):
    '''
    Unparser for twee 2 as HTML
    '''

    def __init__(self, story):
        super().__init__(story)

        self.current = 0
        self.steps   = []

        self.steps.append(UnparserHTML.DataStart(story))

        self.steps.append(UnparserHTML.Style())

        self.steps.append(UnparserHTML.Script())

        if 'tag-colors' in story.data:
            tag_colors = story.data['tag-colors']
            for k, v in tag_colors.items():
                self.steps.append(UnparserHTML.Tag({'name': k, 'color': v}))

        for i, passage in enumerate(story.passages):
            self.steps.append(UnparserHTML.PassageStart(i, passage))
            self.steps.append(UnparserHTML.PassageEnd(passage))

        self.steps.append(UnparserHTML.DataEnd(story))

    def __call__(self):
        if self.current >= len(self.steps):
            return None

        step = self.steps[self.current]
        self.current += 1
        return step()

    def reset(self):
        '''
        Reset the process pipline
        '''
        self.current = 0


    class DataStart:
        '''
        Make the start of the data element
        '''

        def __init__(self, story):
            self.story = story

        def __call__(self):
            attributes = {**self.story.data}
            if 'ifid' not in attributes:
                attributes['ifid'] = uuid.uuid4()

            start_attr = None
            if 'start' in attributes:
                start_attr = attributes['start']
                del attributes['start']

            start_index   = None
            start_passage = None
            start_attrid  = None
            for i, passage in enumerate(self.story.passages):
                if start_attr is not None and start_attr == passage.header.name:
                    start_attrid = i
                    break
                if 'start' == passage.header.name.lower():
                    start_passage = i
                if start_index is None:
                    start_index = i

            startnode = start_attrid
            if startnode is None:
                startnode = start_passage
            if startnode is None:
                startnode = start_index
            if startnode is not None:
                attributes['startnode'] = startnode

            if 'tag-colors' in attributes:
                del attributes['tag-colors']

            attributes = [f'{k}="{v}"' for k, v in attributes.items() if v is not None]
            if len(attributes) == 0:
                attributes = ''
            else:
                attributes = ' ' + ' '.join(attributes)
            return f'<tw-storydata name="{self.story.title}"{attributes}>'


    class DataEnd:
        '''
        Make the end of the data element
        '''

        def __init__(self, story):
            self.story = story

        def __call__(self):
            return '</tw-storydata>'


    class Style:
        '''
        Make the style element
        '''

        def __call__(self):
            return '<style id="twine-user-stylesheet" type="text/twine-css"></style>'


    class Script:
        '''
        Make the script element
        '''

        def __call__(self):
            return '<script id="twine-user-script" type="text/twine-javascript"></script>'


    class Tag:
        '''
        Make the tag element
        '''

        def __init__(self, attributes):
            self.attributes = attributes

        def __call__(self):
            attributes = [f'{k}="{v}"' for k, v in self.attributes.items()]
            if len(attributes) == 0:
                attributes = ''
            else:
                attributes = ' ' + ' '.join(attributes)
            return f'<tw-tag{attributes}></tw-tag>'


    class PassageStart:
        '''
        Make the start of the passage element
        '''

        def __init__(self, pid, passage):
            self.pid     = pid
            self.passage = passage

        def __call__(self):
            return f'<tw-passagedata\
 pid="{self.pid}"\
 name="{self.passage.header.name}">\
{self.passage.context}'


    class PassageEnd:
        '''
        Make the end of the passage element
        '''

        def __init__(self, passage):
            self.passage = passage

        def __call__(self):
            return '</tw-passagedata>'
