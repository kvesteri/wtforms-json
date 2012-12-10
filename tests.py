from pytest import raises
from wtforms import (
    BooleanField,
    FormField,
    IntegerField,
    TextField,
    FieldList,
    Form,
)
from wtforms.form import WebobInputWrapper
from wtforms.validators import Required, Optional
from wtforms_json import (
    flatten_json, init, MultiDict, InvalidData
)


init()


class TestJsonDecoder(object):
    def test_raises_error_if_given_data_not_dict_like(self):
        with raises(InvalidData):
            flatten_json([])

    def test_supports_dicts(self):
        assert flatten_json({'a': False, 'b': 123}) == {'a': False, 'b': 123}

    def test_supports_dicts_with_lists(self):
        assert flatten_json({'a': [1, 2, 3]}) == {'a-0': 1, 'a-1': 2, 'a-2': 3}

    def test_supports_nested_dicts_and_lists(self):
        data = {
            'a': [{'b': True}]
        }
        assert flatten_json(data) == {'a-0-b': True}

    def test_supports_empty_lists(self):
        data = {
            'a': []
        }
        assert flatten_json(data) == {}

    def test_flatten_dict(self):
        assert flatten_json({'a': {'b': {'c': 'd'}}}) == {'a-b-c': 'd'}


class BooleanTestForm(Form):
    is_active = BooleanField(default=False, validators=[Optional()])
    is_confirmed = BooleanField(default=True, validators=[Required()])
    is_private = BooleanField(default=False, validators=[Required()])


class TestPatchedBooleans(object):
    def test_supports_false_values(self):
        form = BooleanTestForm.from_json(
            {'is_active': False, 'is_confirmed': True}
        )
        assert form.patch_data == {
            'is_active': False,
            'is_confirmed': True,
            'is_private': False
        }


class LocationForm(Form):
    name = TextField()
    longitude = IntegerField()
    latitude = IntegerField()


class EventForm(Form):
    name = TextField()
    location = FormField(LocationForm)
    attendees = IntegerField()
    attendee_names = FieldList(TextField())


class TestFormProcessAfterMonkeyPatch(object):
    def test_supports_webob_input_wrapper(self):
        json = {
            'name': 'some patched name'
        }
        form = EventForm(formdata=WebobInputWrapper(MultiDict(json)))
        assert form.data


class TestFormPatchData(object):
    def test_patch_data_with_missing_form_fields(self):
        json = {
            'name': 'some patched name'
        }
        form = EventForm.from_json(json)
        assert form.patch_data == json

    def test_patch_data_for_form_fields(self):
        json = {
            'name': 'some name',
            'location': {
                'name': 'some location'
            }
        }
        form = EventForm.from_json(json)
        assert form.patch_data == json

    def test_supports_field_lists(self):
        json = {
            'name': 'some name',
            'attendee_names': ['Something']
        }
        form = EventForm.from_json(json)
        assert form.patch_data == json

    def test_supports_null_values_for_form_fields(self):
        json = {
            'name': 'some name',
            'location': None
        }
        form = EventForm.from_json(json)
        assert form.patch_data == json

    def test_supports_null_values_for_regular_fields(self):
        json = {
            'name': 'some name',
            'attendees': None
        }
        form = EventForm.from_json(json)
        assert form.patch_data == json
