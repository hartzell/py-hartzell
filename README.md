# py-hartzell

A package that installs my "default" set of python things. Mostly
intended as a demo of how a bioinformatician, group, or department
might manage such things.

This is (intended to be) a well behaved python package and should be
installable by any of the Python tool chains. It follows an
[opinionated][devils-dictionary] set of good practices for packaging
python applications but it doesn't actually *do* anything, it just
brings along its baggage.

## Install

Details depend on your you discover the tarball (might be on PyPi,
might be somewhere local, etc...).

This works:

```sh
# probably want to be in a virtual env, but that's your business....
pip install https://github.com/hartzell/py-hartzell/releases/download/v0.1.2/py-hartzell-0.1.2.tar.gz
```

## Use

This isn't really something you *use*, it's something you *install*
(see above).

That said, you might:

-	depend on a particular version of it ([PEP440] is your
	friend) in your `setup.py`; and
-	perhaps do other cool Python tricks:
	e.g. `import py_hartzell; print py_hartzell.__version__`\)

### Developing

In a virtual environment...

-	`pip install -e .` will set you up in development mode.
-	`pip install pytest-flake8` will install pytest and the pytest-flake8 plugin.
-	`py.test` will run the test suite (multiprocessing and pytest
	require a bit of finnessing to play nicely...)
-	`python setup.py test` will also run the test suite (and doesn't
	require installing the pytest bits by hand).

`py-hartzell` enforces coding style via Flake8. See `.flake8` for its config.

[devils-dictionary]: https://programmingisterrible.com/post/65781074112/devils-dictionary-of-programming
[PEP440]: https://www.python.org/dev/peps/pep-0440/
