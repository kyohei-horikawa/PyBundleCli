# coding: utf-8

from setuptools import setup, find_packages
from py_bundler import __VERSION__


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license_txt = f.read()

setup(
    name='pybundle',
    version=__VERSION__,
    description='bundle python files for command line tools',
    entry_points={
        "console_scripts": [
            "pybundle = py_bundler.py_bundler:main"
        ]
    },
    long_description=readme,
    author='Kyohei Horikawa',
    author_email='kyohei3430@gmail.com',
    url='https://github.com/kyohei-horikawa/py-bundler',
    license=license_txt,
    packages=find_packages(exclude=('sample',))
)
