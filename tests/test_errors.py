from wtforms import Form, IntegerField


class MyForm(Form):
    a = IntegerField()


def test_errors():
    form = MyForm.from_json({'a': 'not an integer!'})
    form.validate()
    assert form.errors == {'a': [u'Not a valid integer value']}
