#!/usr/bin/env python

"""Argv.py

Usage:
    Argv.py [(-v|--verbose)] <arg>...
    Argv.py (-h | --help)
    Argv.py (--version)

Options:
    -v, --verbose                   Show execution details [default: False]
    -h --help                       Show this screen
    --version                       Show version

Example:
    ./Argv.py -v Hello world.

Author: Jonathan D. Lettvin
LinkedIn: jlettvin
Date: 20141020
"""

if __name__ == "__main__":
    from docopt import (docopt)
    from Dict import (Dict)

    def test_old(**kw):
        "This function tests standard dictionary operations."
        kw.update({'title': '\told_dict', 'doc': 'illustrates standard dict'})
        if kw['--verbose']:
            print kw['title'], kw['doc']
            print kw['--verbose']
            print kw['<arg>']

    def test_new(argv):
        "This function test new Dict class dictionary operations."
        argv(title='\tnew_Dict', doc='illustrates new Dict class.')
        if argv.verbose:
            print argv.title, argv.doc
            print argv.verbose
            print argv.arg

    def main():
        "This function is the root of execution."
        kwargs = docopt(__doc__, version="0.0.1")
        argv = Dict(**kwargs)
        test_old(**kwargs)
        test_new(argv)

    main()
