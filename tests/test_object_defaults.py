from wtforms import Form, IntegerField, StringField
from wtforms.validators import Optional


class MyForm(Form):
    a = IntegerField(validators=[Optional()])
    b = StringField()


def test_object_defaults():
    class SomeClass(object):
        a = 1
        b = 'someone'

    form = MyForm.from_json(obj=SomeClass())
    assert form.data == {'a': 1, 'b': 'someone'}


def test_formdata_defaults():
    form = MyForm.from_json({'a': 1, 'b': 'something'})
    assert form.data == {'a': 1, 'b': 'something'}
