Usage
#####


As Command
**********

::

    python -m pytwee tests/t001.tw
    pytwee tests/t001.tw


As Module
*********

::

    import pytwee

    story = pytwee.Story()

    # Parse the .tw/twee file to story
    with open('my-story.tw', 'rt', encoding='utf-8') as f:
        parser = pytwee.twee3.Parser(story)
        for line in iter(f.readline, ''):
            parser(line.rstrip('\n'))
        del parser # don't forget this line

    # Convert the story to twine 2 HTML
    unparser = pytwee.twee2.UnparserHTML(story)
    for line in iter(unparser, None):
        print(line)

    # Convert the story to twine 2 JSON
    unparser = pytwee.twee2.UnparserJSON(story)
    for line in iter(unparser, None):
        print(line)


.. warning::

    You must `del parser` after parsing the last line.
