import flask, flask_sqlalchemy

print('This is working')

app = flask.Flask(__name__)
app.config.from_pyfile('settings.py')
db = flask_sqlalchemy.SQLAlchemy(app)