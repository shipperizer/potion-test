from flask_potion import ModelResource, fields
from flask_potion.routes import Relation

from potion_test.models import Alpha, Beta


class AlphaResource(ModelResource):
    betas = Relation('beta')

    class Meta:
        name = 'alpha'
        model = Alpha

    class Schema:
        betas = fields.ToMany('beta', io='r')


class BetaResource(ModelResource):
    class Meta:
        name = 'beta'
        model = Beta

    class Schema:
        alpha_id = fields.Integer(io='wr')
