from potion_test.db import db


class Alpha(db.Model):
    __tablename__ = 'alpha'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    betas = db.relationship('Beta', backref='alpha')


class Beta(db.Model):
    __tablename__ = 'beta'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    alpha_id = db.Column(db.Integer, db.ForeignKey('alpha.id'), nullable=False)
