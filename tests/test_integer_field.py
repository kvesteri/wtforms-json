import pytest
from wtforms import Form, IntegerField
from wtforms.validators import InputRequired


class TestIntegerField(object):
    @pytest.mark.parametrize(
        'value',
        ('0', 0)
    )
    def test_validation_with_input_required(self, value):
        class MyForm(Form):
            a = IntegerField(validators=[InputRequired()])

        assert MyForm.from_json({'a': value}).validate()
