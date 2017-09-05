argparse_tutorial
=================

code from ``argparse`` tutorial and documentation

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
    - `parent parser`_

tests
-----

.. code::

    python3 -m unittest doctests.py

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
