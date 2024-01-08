import uuid
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Business(db.Model):
    """Business model"""
    pkid = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    id = db.Column(db.String(36), default=str(uuid.uuid4()), unique=True, nullable=False)
    company_name = db.Column(db.String(120), unique=True, nullable=False)
    industry = db.Column(db.String(120), unique=False, nullable=False)
    target_audience = db.Column(db.String(120), unique=False, nullable=False)
    unique_selling_points = db.Column(db.String(120), unique=False, nullable=False)
    key_products_services = db.Column(db.String(120), unique=False, nullable=False)
    tone_style_preferences = db.Column(db.String(120), unique=False, nullable=False)
    description = db.Column(db.String(120), unique=False, nullable=False)
    address = db.Column(db.String(120), unique=False, nullable=False)
    phone = db.Column(db.String(120), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    website = db.Column(db.String(120), unique=True, nullable=False)
    category = db.Column(db.String(120), unique=False, nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('businesses', lazy=True))

    def __repr__(self):
        return '<Business %r>' % self.name


