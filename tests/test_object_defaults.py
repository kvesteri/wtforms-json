from wtforms import Form, IntegerField, TextField


def test_object_defaults():
    class SomeClass(object):
        a = 1
        b = 'someone'

    class MyForm(Form):
        a = IntegerField()
        b = TextField()

    form = MyForm(obj=SomeClass())
    assert form.data == {'a': 1, 'b': 'someone'}
