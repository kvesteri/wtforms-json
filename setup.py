"""
wtforms-json
-------------------

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
    name='wtforms-json',
    version='0.1.0',
    url='https://github.com/kvesteri/wtforms-json',
    license='BSD',
    author='Konsta Vesterinen',
    author_email='konsta@fastmonkeys.com',
    description=__doc__,
    long_description=__doc__,
    packages=['wtforms_json'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'WTForms>=1.0.1'
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
