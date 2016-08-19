from init import db, app

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data = db.Column(db.String(20))

db.create_all(app=app)