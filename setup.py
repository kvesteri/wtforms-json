"""
WTForms-JSON
------------

Adds smart json support for WTForms. Useful for when using WTForms with RESTful
APIs.
"""

from setuptools import setup, Command
import subprocess


class PyTest(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        errno = subprocess.call(['py.test'])
        raise SystemExit(errno)

setup(
    name='WTForms-JSON',
    version='0.2.4',
    url='https://github.com/kvesteri/wtforms-json',
    license='BSD',
    author='Konsta Vesterinen',
    author_email='konsta@fastmonkeys.com',
    description=(
        'Adds smart json support for WTForms. Useful for when using'
        ' WTForms with RESTful APIs.'
    ),
    long_description=__doc__,
    packages=['wtforms_json'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'WTForms>=1.0.2',
        'six>=1.3.0'
    ],
    cmdclass={'test': PyTest},
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
