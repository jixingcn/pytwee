Usage
#####

Story from twee 3
*****************

::

    import pytwee

    story = pytwee.Story()

    with open('my-story.tw', 'rt', encoding='utf-8') as f:
        parser = pytwee.twee3.Parser(story)
        for line in iter(f.readline, ''):
            parser(line)
        del parser # don't forget this line


Story to twee 2 HTML
********************

::

    import pytwee

    story = pytwee.Story()

    unparser = pytwee.twee2.UnparserHTML(story)
    for line in iter(unparser, None):
        print(line)
