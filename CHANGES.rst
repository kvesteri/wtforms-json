Changelog
---------

Here you can see the full list of changes between each WTForms-JSON release.


0.3.4 (2022-02-22)
^^^^^^^^^^^^^^^^^^

- Added Python 3.10 support (#61, pull request courtesy keaysma)


0.3.3 (2017-07-07)
^^^^^^^^^^^^^^^^^^

- Update WTForms requirement (#51, pull request courtesy quantus)


0.3.2 (2017-07-05)
^^^^^^^^^^^^^^^^^^

- Use wtforms_alchemy for importing QuerySelectField if it is installed (#50, pull request courtesy Lee-W)


0.3.1 (2017-03-05)
^^^^^^^^^^^^^^^^^^

- Fixed default value handling for StringField (#49, pull request courtesy noirbizarre)
- Added py36 to test matrix


0.3.0 (2016-08-30)
^^^^^^^^^^^^^^^^^^

- Added support for WTForms 3.0
- Dropped Python 2.6 support


0.2.10 (2015-03-28)
^^^^^^^^^^^^^^^^^^

- Fixed process_formdata support for python3
- Added flake8 and isort checks


0.2.9 (2015-02-28)
^^^^^^^^^^^^^^^^^^

- Fixed inheritance handling with FieldLists and FormFields


0.2.8 (2014-09-21)
^^^^^^^^^^^^^^^^^^

- Fixed falsy boolean value handling


0.2.7 (2014-09-01)
^^^^^^^^^^^^^^^^^^

- Only flatten dict if field is an instance of FormField


0.2.6 (2014-05-24)
^^^^^^^^^^^^^^^^^^

- Made ``skip_unknown_keys=True`` prevent raising errors from keys that exist in
  form class but are not form fields


0.2.5 (2013-12-16)
^^^^^^^^^^^^^^^^^^

- Fixed ``skip_unknown_keys`` option passing from ``from_json`` to
  ``flatten_json`` (#17)


0.2.4 (2013-11-17)
^^^^^^^^^^^^^^^^^^

- Fixed object value setting in ``from_json``
- Prepared support for WTForms 2.0


0.2.3 (2013-11-11)
^^^^^^^^^^^^^^^^^^

- Added support for ``QuerySelectField`` and ``QuerySelectMultipleField``


0.2.2 (2013-08-30)
^^^^^^^^^^^^^^^^^^

- Configurable unknown json key handling


0.2.1 (2013-08-19)
^^^^^^^^^^^^^^^^^^

- Custom ``SelectField`` support


0.2.0 (2013-07-26)
^^^^^^^^^^^^^^^^^^

- Rewritten ``flatten_json`` (now supports ``SelectMultipleField``s)


0.1.5 (2013-07-25)
^^^^^^^^^^^^^^^^^^

- Added enhanced unicode coercion
- Package six added to requirements


0.1.4 (2013-03-16)
^^^^^^^^^^^^^^^^^^

- Updated WTForms requirements



0.1.3 (2013-03-01)
^^^^^^^^^^^^^^^^^^

- Fixed 'First example' in docs
