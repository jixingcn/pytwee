pytwee
######

|pylint-action| |test-action| |pypi-action|

|pypi-version| |pypi-python| |pypi-status|

|docs-badge|


Features
********

- Parse the **.twee** file with `twee 3 spec <https://github.com/iftechfoundation/twine-specs/blob/master/twee-3-specification.md>`_
- Convert the **Story** to `twine 2 HTML spec <https://github.com/iftechfoundation/twine-specs/blob/master/twine-2-htmloutput-spec.md>`_
- Convert the **Story** to `twine 2 JSON doc <https://github.com/iftechfoundation/twine-specs/blob/master/twine-2-jsonoutput-doc.md>`_
- Run as a command


Use
***

::

    # Install by pip
    $ python -m pip install pytwee

::

    # Run in console
    $ python -m pytwee tests/t001.tw

::

    # Import as a module
    import pytwee

    story = pytwee.story.Story()

    with open('my-story.tw', 'rt') as f:
        parser = pytwee.twee3.Parser(story)
        for line in iter(f.readline, ''):
            parser(line)
        del parser #<- very important

    print('story:', story)


License
*******

|license|



.. |pylint-action| image:: https://img.shields.io/github/actions/workflow/status/jixingcn/pytwee/pylint.yml?label=pylint
    :alt: pylint workflow Status
    :target: https://github.com/jixingcn/pytwee/actions/workflows/pylint.yml


.. |test-action| image:: https://img.shields.io/github/actions/workflow/status/jixingcn/pytwee/test.yml?label=test
    :alt: test workflow Status
    :target: https://github.com/jixingcn/pytwee/actions/workflows/test.yml


.. |pypi-action| image:: https://img.shields.io/github/actions/workflow/status/jixingcn/pytwee/pypi.yml?label=pypi
    :alt: pypi workflow Status
    :target: https://github.com/jixingcn/pytwee/actions/workflows/pypi.yml


.. |pypi-version| image:: https://img.shields.io/pypi/v/pytwee
    :alt: PyPI - Version
    :target: https://pypi.org/project/pytwee


.. |pypi-status| image:: https://img.shields.io/pypi/status/pytwee
    :alt: PyPI - Status
    :target: https://pypi.org/project/pytwee


.. |pypi-python| image:: https://img.shields.io/pypi/pyversions/pytwee
    :alt: PyPI - Python Version
    :target: https://pypi.org/project/pytwee


.. |docs-badge| image:: https://img.shields.io/readthedocs/pytwee/latest
    :alt: Read the Docs (version)
    :target: https://pytwee.readthedocs.io

 
.. |license| image:: https://img.shields.io/badge/license-MIT-green
    :alt: Static Badge
    :target: https://github.com/jixingcn/pytwee/blob/main/LICENSE

