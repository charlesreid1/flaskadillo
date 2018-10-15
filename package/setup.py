from setuptools import setup

"""
setup.py for the simplest flask package,
the simplest python package you can imagine that contains a flask app.
"""

version="1.0"

config = {
    'description': 'simple',
    'version' : version,
    'install_requires': ['flask'],
    'include_package_data' : True,
    'test_suite': 'nose.collector',
    'tests_require': ['nose'],
    'packages': ['simple','simple.webapp'],
    'package_dir' : {
        'simple' : 'src',
        'simple.webapp' : 'src/webapp'
    },
    'scripts': [],
    'name': 'simple',
    'zip_safe' : False
}

setup(**config)
