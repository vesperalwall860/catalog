from . import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    price = db.Column(db.Float)
    url = db.Column(db.String)
    images = db.Column(db.Text)
    chars = db.Column(db.Text)
