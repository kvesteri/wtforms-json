import collections

from wtforms import Form
from wtforms.fields import BooleanField, Field, FormField, _unset_value
from wtforms.validators import Optional, Required


def flatten_json(json, parent_key='', separator='-'):
    items = []
    for key, value in json.items():
        new_key = parent_key + separator + key if parent_key else key
        if isinstance(value, collections.MutableMapping):
            items.extend(flatten_json(value, new_key).items())
        elif isinstance(value, list):
            items.extend(flatten_json_list(value, new_key))
        else:
            items.append((new_key, value))
    return dict(items)


def flatten_json_list(json, parent_key='', separator='-'):
    items = []
    i = 0
    for item in json:
        new_key = parent_key + separator + str(i)
        if isinstance(item, list):
            items.extend(flatten_json_list(item, new_key, separator))
        elif isinstance(item, dict):
            items.extend(flatten_json(item, new_key, separator).items())
        else:
            items.append((new_key, item))
        i += 1
    return items


@property
def patch_data(self):
    data = {}

    def is_optional(field):
        return Optional in [v.__class__ for v in field.validators]

    def is_required(field):
        return Required in [v.__class__ for v in field.validators]

    for name, f in self._fields.iteritems():
        if f.is_missing:
            if is_optional(f):
                continue
            elif not is_required(f) and f.default is None:
                continue
        data[name] = f.data
    return data


def monkey_patch_process(func):
    """Monkey patches Form process method to better understand missing values.
    """
    def process(self, formdata, data=_unset_value):
        if isinstance(self, FormField):
            pass
        else:
            self.is_missing = True
            if formdata:
                if self.name in formdata:
                    self.is_missing = not bool(formdata.getlist(self.name))
                else:
                    self.is_missing = True
        func(self, formdata, data=data)
    return process


@property
def is_missing(self):
    for name, field in self._fields.items():
        if not field.is_missing:
            return False
    return True


def process_formdata(self, valuelist):
    """This function should overrides BooleanField process_formdata in order
    to adds support for JSON styled boolean False values."""
    if valuelist and valuelist[0] is False:
        self.data = False
    else:
        self.data = bool(valuelist)


def init():
    Form.is_missing = is_missing
    Form.patch_data = patch_data
    Field.process = monkey_patch_process(Field.process)
    FormField.process = monkey_patch_process(FormField.process)
    BooleanField.process_formdata = process_formdata
