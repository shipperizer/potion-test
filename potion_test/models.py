from potion_test.db import db


class TestA(db.Model):
    __tablename__ = 'test_a'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    test_bs = db.relationship('TestB', backref='test_a')


class TestB(db.Model):
    __tablename__ = 'test_b'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    test_a_id = db.Column(db.Integer, db.ForeignKey('test_a.id'), nullable=False)
