#!/bin/bash

bumpversion minor #bump version in all files + create commit
python setup.py sdist bdist_wheel --universal
twine upload dist/--tar.gz dist/..whl
