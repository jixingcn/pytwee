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

        if 'tag-colors' in story.data:
            tag_colors = story.data['tag-colors']
            for k, v in tag_colors.items():
                self.steps.append(UnparserHTML.Tag({'name': k, 'color': v}))

        script_passage_ids = [i for i, p in enumerate(story.passages) if 'script' in p.header.tags]
        for i in script_passage_ids:
            self.steps.append(UnparserHTML.Script(story.passages[i]))

        stylesheet_passage_ids = [i for i, p in enumerate(story.passages) if 'stylesheet' in p.header.tags]
        for i in stylesheet_passage_ids:
            self.steps.append(UnparserHTML.Stylesheet(story.passages[i]))

        for i, passage in enumerate(story.passages):
            if i in script_passage_ids:
                continue
            if i in stylesheet_passage_ids:
                continue
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
            # Copy the attributes from the story
            attributes = {**self.story.data}

            if 'ifid' not in attributes:
                attributes['ifid'] = uuid.uuid4()

            # Find the startnode's value
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

            # Remove the tag-colors from attributes
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


    class Stylesheet:
        '''
        Make the stylesheet element
        '''

        def __init__(self, passage):
            self.passage = passage

        def __call__(self):
            element_id = ''
            if self.passage.header.name != '':
                element_id = f' id="{self.passage.header.name}"'
            return f'<style{element_id} type="text/twine-css">{self.passage.context}</style>'


    class Script:
        '''
        Make the script element
        '''

        def __init__(self, passage):
            self.passage = passage

        def __call__(self):
            element_id = ''
            if self.passage.header.name != '':
                element_id = f' id="{self.passage.header.name}"'
            return f'<script{element_id} type="text/twine-javascript">{self.passage.context}</script>'


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
            attributes = {
                'pid': self.pid,
                'name': self.passage.header.name,
                }
            if len(self.passage.header.tags) > 0:
                attributes['tags'] = ' '.join(self.passage.header.tags)
            attributes = {
                **attributes,
                **self.passage.header.metadata,
            }
            attributes = ' ' + ' '.join([f'{k}="{v}"' for k, v in attributes.items()])
            return f'<tw-passagedata{attributes}>\
{self.passage.context}'


    class PassageEnd:
        '''
        Make the end of the passage element
        '''

        def __init__(self, passage):
            self.passage = passage

        def __call__(self):
            return '</tw-passagedata>'


class UnparserJSON(twee.Unparser):
    '''
    Unparser for twee 2 as HTML
    '''

    def __init__(self, story):
        super().__init__(story)

        self.current = 0
        self.steps   = []

        self.steps.append(UnparserJSON.Data(story))

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


    class Data:
        '''
        Make the start of the data element
        '''

        def __init__(self, story):
            self.story = story

        def __call__(self):
            jstory = {
                'name': self.story.title,
                **self.story.data,
            }

            if 'ifid' not in jstory:
                jstory['ifid'] = uuid.uuid4()
            jstory['ifid'] = str(jstory['ifid'])

            if len(self.story.passages) > 0:
                jpassages = []
                for passage in self.story.passages:
                    if 'script' in passage.header.tags:
                        if 'script' not in jstory:
                            jstory['script'] = passage.context
                        else:
                            jstory['script'] += '\n' + passage.context
                    elif 'stylesheet' in passage.header.tags:
                        if 'style' not in jstory:
                            jstory['style'] = passage.context
                        else:
                            jstory['style'] += '\n' + passage.context
                    else:
                        jpassage = {
                            'name': passage.header.name,
                        }
                        if len(passage.header.tags) > 0:
                            jpassage['tags'] = passage.header.tags
                        if len(passage.header.metadata) > 0:
                            jpassage['metadata'] = passage.header.metadata
                        jpassage['text'] = passage.context
                        jpassages.append(jpassage)
                jstory['passages'] = jpassages

            return jstory
