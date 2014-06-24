pycodegolf
==========

A relaxed code golf evaluator for python code. Currently both whitespace and
whole comment lines are stripped from the count so you can be happy to keep
some degree of legibility.


Usage
-----

Either put the pygolf.py file in your path or run from this location with
something like:

```sh
path/to/pygolf.py potentially/different/path/to/examplefile
```

e.g.

```sh
./pygolf.py pygolf.py
```

currently outputs

```
97
```

Limitations
-----------

This should not be used to
* evaluate multi-file solutions.
* evaluate code written in a language where # is not used at the beginning of a line to indicate a whole line comment

Additionally:
* in-line comments are kept in the line count - # has to be the first character in a line to be ignored
* using python's triple quoted strings as a form of comment will also be included in the final total
* lines in a triple quoted string with # as the first character in a line will be excluded from the count
