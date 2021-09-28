from setuptools import find_packages
from setuptools import setup


setup(
    name='jowo_pre_commit_hooks',
    description='Some hooks for pre-commit.',
    url='https://github.com/jonasundderwolf/pre-commit-hooks',
    version='1.0.0',
    author="Jonas und der Wolf GmbH",
    author_email="opensource@jonasundderwolf.de",

    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    packages=find_packages(exclude=('tests*', 'testing*')),
    install_requires=[
        'flake8',
        'pyyaml',
        'six',
    ],
    entry_points={
        'console_scripts': [
            'check-branch-name-length = pre_commit_hooks.check_branch_name_length:main',
        ],
    },
)
