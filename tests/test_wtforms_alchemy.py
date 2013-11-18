import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from wtforms_alchemy import ModelForm
import wtforms_json

wtforms_json.init()

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


def test_init_formdata():
    json = {
        'a': u'First Event',
        'b': u'Second',
        'c': u'Third',
        'd': u'Fourth'
    }

    form = TestForm.from_json(json)
    assert form.data == json
