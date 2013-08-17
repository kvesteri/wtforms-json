from wtforms import (
    Form,
    IntegerField,
    SelectMultipleField,
    TextField,
)
from wtforms.validators import IPAddress


class TestFieldTypeCoercion(object):
    def test_integer_to_unicode_coercion(self):
        class NetworkForm(Form):
            address = TextField('Address', [IPAddress()])

        network = dict(address=123)

        form = NetworkForm.from_json(network)
        assert not form.validate()

    def test_integer_coercion(self):
        class UserForm(Form):
            age = IntegerField('age')

        network = dict(age=123)

        form = UserForm.from_json(network)
        assert form.validate()


class FooForm(Form):
    items = SelectMultipleField(
        choices=(
            (1, 'a'),
            (2, 'b'),
            (3, 'c'),
        ),
        coerce=int
    )


class TestSelectMultipleField(object):
    def test_from_json(self):
        data = {'items': [1, 3]}
        form = FooForm.from_json(data)
        assert form.validate()
        assert form.items.data
