from pytest import raises
from wtforms import (
    BooleanField,
    FieldList,
    FormField,
    Form,
    IntegerField,
    SelectMultipleField,
    TextField,
)
from wtforms_json import flatten_json, InvalidData


class TestJsonDecoder(object):
    def test_raises_error_if_given_data_not_dict_like(self):
        class MyForm(Form):
            pass
        with raises(InvalidData):
            flatten_json(MyForm, [])

    def test_unknown_attribute(self):
        class MyForm(Form):
            a = BooleanField()

        with raises(InvalidData):
            flatten_json(MyForm, {'b': 123})

    def test_supports_dicts(self):
        class MyForm(Form):
            a = BooleanField()
            b = IntegerField()

        assert (
            flatten_json(MyForm, {'a': False, 'b': 123}) ==
            {'a': False, 'b': 123}
        )

    def test_supports_select_multiple_field_decoding(self):
        class MyForm(Form):
            a = SelectMultipleField()

        assert flatten_json(MyForm, {'a': [1, 2, 3]}) == {'a': [1, 2, 3]}

    def test_supports_field_list_decoding(self):
        class MyForm(Form):
            a = FieldList(TextField())

        assert flatten_json(MyForm, {'a': [1, 2, 3]}) == {
            'a-0': 1,
            'a-1': 2,
            'a-2': 3
        }

    def test_supports_nested_dicts_and_lists(self):
        class OtherForm(Form):
            b = BooleanField()

        class MyForm(Form):
            a = FieldList(FormField(OtherForm))
        data = {
            'a': [{'b': True}]
        }
        assert flatten_json(MyForm, data) == {'a-0-b': True}

    def test_flatten_dict(self):
        class DeeplyNestedForm(Form):
            c = TextField()

        class NestedForm(Form):
            b = FormField(DeeplyNestedForm)

        class MyForm(Form):
            a = FormField(NestedForm)

        assert flatten_json(MyForm, {'a': {'b': {'c': 'd'}}}) == {
            'a-b-c': 'd'
        }
