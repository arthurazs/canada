# coding: utf-8
'''Setup for dotapatch.'''
from setuptools import setup

APP_NAME = 'canada'

try:
    with open('README.rst', 'r') as readme:
        APP_LONG_DESCRIPTION = readme.read()
except IOError as err:
    print('ERROR README.rst not found')
    print(err)
    APP_LONG_DESCRIPTION = ''

APP_URL = 'https://github.com/arthurazs/{}/'.format(APP_NAME)

setup(
    name=APP_NAME,
    version='0.1.0',
    author='Arthur Zopellaro',
    author_email='arthurazsoares@gmail.com',
    description=('Canada game.'),
    license='MIT',
    keywords=(
        'game canada'
    ),
    url=APP_URL,
    packages=['game', 'tests'],
    long_description=APP_LONG_DESCRIPTION,
    python_requires='>=3.6, <3.7',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Games/Entertainment',
    ],
    setup_requires=['nose>=1.3.7', 'rednose>=1.3.0'],
    entry_points={
        'console_scripts': [
            '{0} = {1}.__main__:main'.format(APP_NAME, 'game')]
    },
    tests_require=['coverage>=4.4.2'],
)
