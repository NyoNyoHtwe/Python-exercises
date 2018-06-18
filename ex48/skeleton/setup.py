try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'description': 'My Progect',
        'author': 'My Name',
        'url':'URl to get it at.',
        'download_url': 'Where to download it.',
        'author_email': 'My email',
        'version': '0.1',
        'install_requires': ['nose'],
        'package': ['lexicon'],
        'scripts': [],
        'name': 'projectname'
        }

setup(**config)

