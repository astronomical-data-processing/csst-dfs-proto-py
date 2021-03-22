# coding: utf-8
"""Setup config file to package the configuration database."""
from os import walk, listdir
from setuptools import find_packages
from os.path import join
from setuptools import setup
import csst_proto


def package_files(directory):
    """Get list of data files to add to the package."""
    paths = []
    for (path, _, file_names) in walk(directory):
        for filename in file_names:
            paths.append(join('..', path, filename))
    return paths


with open('README.md', 'r') as file:
    LONG_DESCRIPTION = file.read()

setup(name='csst_dfs_proto',
      version=csst_proto.__version__,
      author='CSST DFS team.',
      description='CSST DFS Base Proto library.',
      long_description=LONG_DESCRIPTION,
      long_description_content_type='text/markdown',
      url='',
      packages=find_packages(exclude=('test', 'test.*', 'fabfile')),
      install_requires=[
          'grpcio==1.28.1'
      ],
      zip_safe=False,
      classifiers=[
          "Programming Language :: Python :: 3 :: Only",
          "Development Status :: 1 - Planning",
          "License :: OSI Approved :: BSD License"
      ]
)
