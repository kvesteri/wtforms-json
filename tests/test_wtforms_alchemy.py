import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from wtforms_alchemy import ModelForm

engine = create_engine('sqlite:///:memory:')
Base = declarative_base(engine)
Session = sessionmaker(bind=engine)
session = Session()


class Test(Base):
    __tablename__ = 'test'

    id = sa.Column(sa.BigInteger, autoincrement=True, primary_key=True)
    a = sa.Column(sa.Unicode(100), nullable=True)
    b = sa.Column(sa.Unicode(255), nullable=True)
    c = sa.Column(sa.Unicode(100), nullable=True)
    d = sa.Column(sa.Unicode(255), nullable=True)


class TestForm(ModelForm):
    class Meta:
        model = Test

Base.metadata.create_all(engine)
# Example


def create_form_from_json(**kwargs):
    if not kwargs.get('json'):
        kwargs['json'] = {
            'a': u'First Event',
            'b': u'Second',
            'c': u'Third',
            'd': u'Fourth'
        }
    return TestForm.from_json(kwargs['json'])


def create_populated_obj_from_json_form():
    form = create_form_from_json()
    obj = Test()
    form.populate_obj(obj)
    return obj


def test_init_formdata():
    json = {
        'a': u'First Event',
        'b': u'Second',
        'c': u'Third',
        'd': u'Fourth'
    }
    form = create_form_from_json(json=json)
    assert form.data == json


def test_populate_form_from_object():
    obj = create_populated_obj_from_json_form()
    form = TestForm(obj=obj)
    assert len(form.data) == 4
    for key in form.data:
        assert form.data[key] == obj.__dict__[key]
