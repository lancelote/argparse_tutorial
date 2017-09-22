.. image:: https://requires.io/github/lancelote/argparse_tutorial/requirements.svg?branch=master
    :target: https://requires.io/github/lancelote/argparse_tutorial/requirements/?branch=master

.. image:: https://travis-ci.org/lancelote/argparse_tutorial.svg?branch=master
    :target: https://travis-ci.org/lancelote/argparse_tutorial

argparse_tutorial
=================

code from ``argparse`` tutorial and documentation

tests
-----

.. code::

    make test

table of content
----------------

- `argparse tutorial`_
    - `basics`_
    - `positional arguments`_
    - `document arguments`_ and specify the type
    - `optional arguments`_
    - `boolean optional arguments`_
    - `short options`_
    - `positional and optional arguments`_
    - `processing multiple argument values`_
    - `limit number of allowed values for argument`_
    - `countable arguments`_, e.g. ``-vvv`` and default value
    - `add more arguments`_
    - `add more text to verbose`_
    - `conflicting options`_
    - `description`_
- `examples from documentation`_
    - `simple example`_
    - `parent parser`_, parsers share multiple arguments
    - `epilog message in help`_
    - `overwrite usage message`_
    - `provide a description for parser`_
    - `class mixin for help formatting`_
    - `change flags prefix character`_
    - `load arguments from file`_
    - `default value for all parser arguments`_, suppressing default ``None``
    - `disallow abbreviation in arguments`_
    - `allow conflict flags`_
    - `disable help flag`_ or change it's prefix
    - `optional and positional arguments`_
    - `different add_argument actions`_
    - `number of arguments`_
    - `default value for argument`_
    - `argument type conversion`_
    - `arguments with choices`_
    - `required arguments`_
    - `providing a help`_
    - `display example value in help`_
    - `changing inner option reference name`_
    - `optional value syntax`_
    - `invalid arguments messages`_
    - `dash in argument name`_
    - `argument abbreviations`_
    - `interactive parse_args`_
    - `Namespace object`_

.. _argparse tutorial: https://docs.python.org/3/howto/argparse.html
.. _basics: tutorial/basics.py
.. _positional arguments: tutorial/positional_arguments.py
.. _document arguments: tutorial/document_arguments.py
.. _optional arguments: tutorial/optional_arguments.py
.. _boolean optional arguments: tutorial/optional_arguments.py
.. _short options: tutorial/short_options.py
.. _positional and optional arguments: tutorial/positional_and_optional.py
.. _processing multiple argument values: tutorial/process_different_arg_values.py
.. _limit number of allowed values for argument: tutorial/strict_set_of_args_values.py
.. _countable arguments: tutorial/countable_arguments.py
.. _add more arguments: tutorial/more_arguments.py
.. _add more text to verbose: tutorial/more_verbose_text.py
.. _conflicting options: tutorial/conflicting_options.py
.. _description: tutorial/description.py
.. _examples from documentation: https://docs.python.org/3/library/argparse.html
.. _simple example: documentation/simple_example.py
.. _parent parser: documentation/parents.py
.. _epilog message in help: documentation/epilog.py
.. _overwrite usage message: documentation/usage.py
.. _provide a description for parser: documentation/parser_description.py
.. _class mixin for help formatting: documentation/formatter_class.py
.. _change flags prefix character: documentation/prefix_chars.py
.. _load arguments from file: documentation/fromfile_prefix_chars.py
.. _default value for all parser arguments: documentation/argument_default.py
.. _disallow abbreviation in arguments: documentation/allow_abbrev.py
.. _allow conflict flags: documentation/conflict_handler.py
.. _disable help flag: documentation/add_help.py
.. _optional and positional arguments: documentation/name_or_flags.py
.. _different add_argument actions: documentation/action.py
.. _number of arguments: documentation/nargs.py
.. _default value for argument: documentation/default.py
.. _argument type conversion: documentation/convert_type.py
.. _arguments with choices: documentation/choices.py
.. _required arguments: documentation/required.py
.. _providing a help: documentation/help.py
.. _display example value in help: documentation/metavar.py
.. _changing inner option reference name: documentation/dest.py
.. _optional value syntax: documentation/optional.py
.. _invalid arguments messages: documentation/invalid.py
.. _dash in argument name: documentation/dash.py
.. _argument abbreviations: documentation/abbreviations.py
.. _interactive parse_args: documentation/parse_args.py
.. _Namespace object: documentation/namespace.py
