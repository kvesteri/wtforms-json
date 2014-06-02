from pytest import raises
from wtforms import (
    BooleanField,
    FieldList,
    Form,
    FormField,
    IntegerField,
    StringField,
)
from wtforms.validators import DataRequired, Optional
from wtforms_json import MultiDict, InvalidData


class BooleanTestForm(Form):
    is_active = BooleanField(default=False, validators=[Optional()])
    is_confirmed = BooleanField(default=True, validators=[DataRequired()])
    is_private = BooleanField(default=False, validators=[DataRequired()])


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
    name = StringField()
    longitude = IntegerField()
    latitude = IntegerField()


class EventForm(Form):
    name = StringField()
    location = FormField(LocationForm)
    attendees = IntegerField()
    attendee_names = FieldList(StringField())


class TestSkipUnknownKeys(object):
    def test_skips_unknown_keys(self):
        json = {
            'name': 'some patched name',
            'unknown': 'something'
        }
        with raises(InvalidData):
            EventForm.from_json(json, skip_unknown_keys=False)


class TestFormProcessAfterMonkeyPatch(object):
    def test_supports_webob_input_wrapper(self):
        json = {
            'name': 'some patched name'
        }
        form = EventForm(formdata=MultiDict(json))
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


class OptionalTestForm(Form):
    can_be_null = StringField(
        validators=[Optional(nullable=True, blank=False)]
    )
    can_be_blank = StringField(
        validators=[Optional(nullable=False, blank=True)]
    )
    can_be_both = StringField(validators=[Optional()])
    can_be_missing = StringField(
        validators=[Optional(nullable=False, blank=False)]
    )


class TestPatchOptionalValidator(object):
    def test_all_pass(self):
        json = {
            'can_be_null': None,
            'can_be_blank': '',
            'can_be_both': None,
            'can_be_missing': 'here',
        }
        form = OptionalTestForm.from_json(json)
        assert form.validate() == True
        assert form.patch_data == json

    def test_missing_fail_because_null(self):
        json = {
            'can_be_missing': None,
        }
        errors = {
            'can_be_missing': ['This field can not be null.'],
        }
        form = OptionalTestForm.from_json(json)
        assert form.validate() == False
        assert form.errors == errors

    def test_missing_fail_because_blank(self):
        json = {
            'can_be_missing': '',
        }
        errors = {
            'can_be_missing': ['This field can not be blank.'],
        }
        form = OptionalTestForm.from_json(json)
        assert form.validate() == False
        assert form.errors == errors

    def test_missing_pass_when_missing(self):
        json = {
            'can_be_null': None,
            'can_be_blank': '',
            'can_be_both': '',
        }
        form = OptionalTestForm.from_json(json)
        assert form.validate() == True
        assert form.patch_data == json

    def test_nullable_fail_when_blank(self):
        json = {
            'can_be_null': '',
        }
        errors = {
            'can_be_null': ['This field can not be blank.'],
        }
        form = OptionalTestForm.from_json(json)
        assert form.validate() == False
        assert form.errors == errors

    def test_blank_fail_because_null(self):
        json = {
            'can_be_blank': None,
        }
        errors = {
            'can_be_blank': ['This field can not be null.'],
        }
        form = OptionalTestForm.from_json(json)
        assert form.validate() == False
        assert form.errors == errors

    def test_blank_fail_when_whitespace(self):
        json = {
            'can_be_null': ' ',
        }
        errors = {
            'can_be_null': ['This field can not be blank.'],
        }
        form = OptionalTestForm.from_json(json)
        assert form.validate() == False
        assert form.errors == errors
