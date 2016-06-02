from flask_potion import ModelResource, fields
from flask_potion.routes import Relation

from potion_test.models import TestA, TestB


class TestAResource(ModelResource):
    test_bs = Relation('test_b')

    class Meta:
        name = 'test_a'
        model = TestA

    class Schema:
        test_bs = fields.ToMany('test_b', io='r')


class TestBResource(ModelResource):
    class Meta:
        name = 'test_b'
        model = TestB

    class Schema:
        test_a_id = fields.Integer(io='wr')
