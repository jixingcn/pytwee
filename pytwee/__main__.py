'''
pytwee cmd
'''

import argparse
import sys

from .      import __version__
from .story import Story
from .      import twee2
from .      import twee3


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog        = 'pytwee',
        description = '\n'.join([
            'parse/convert the .tw/.twee file.',
            f'v{__version__}',
            ]),
        )

    parser.add_argument(
        'inputfile',
        type = argparse.FileType('rt', encoding='utf-8'),
        help = 'Input .tw/.twee file path',
        )

    parser.add_argument(
        '-ot', '--outputtype',
        choices = ['twee2html', 'twee2json'],
        default = 'twee2html',
        help    = 'Output file type',
        )

    parser.add_argument(
        '-o', '--outputfile',
        type = argparse.FileType('wt', encoding='utf-8'),
        help='Output file path',
        )

    args = parser.parse_args()

    story = Story()

    parser = twee3.Parser(story)
    for line in iter(args.inputfile.readline, ''):
        parser(line)
    del parser

    if args.outputtype == 'twee2html':
        unparser = twee2.UnparserHTML(story)

        def outputfunc(l):
            '''Print to console'''
            print(l)

        if args.outputfile is not None:
            outputfunc = args.outputfile.write

        for line in iter(unparser, None):
            outputfunc(line)
    elif args.outputtype == 'twee2json':
        unparser = twee2.UnparserJSON(story)

        def outputfunc(l):
            '''Print to console'''
            print(l)

        if args.outputfile is not None:
            outputfunc = args.outputfile.write

        for jobj in iter(unparser, None):
            outputfunc(jobj)
    else:
        raise NotImplementedError('Not ready for this!')

    sys.exit(0)
