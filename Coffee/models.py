from Coffee import db


class Coffee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.String(6))
    structure = db.Column(db.Text)

    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)

    def __repr__(self):
        return '<Coffee %r>' % id