#!/bin/bash

bumpversion

python setup.py sdist bdist_wheel --universal

twine upload dist/--tar.gz dist/..whl
