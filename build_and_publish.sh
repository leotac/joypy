#!/bin/bash

set -e
rm -rf dist
#bumpversion patch #major minor patch - bump version in all files
python setup.py sdist bdist_wheel --universal
twine upload dist/**tar.gz dist/**whl
rm -rf dist
